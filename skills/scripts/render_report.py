#!/usr/bin/env python3
"""Render a bounded SpyTrend report without network or shell execution."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import ipaddress
import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LANGUAGE_RE = re.compile(r"^[A-Za-z]{2,8}(?:-[A-Za-z0-9]{1,8})*$")
FORMATS = {"markdown", "html", "both"}
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "report.schema.json"
REPORT_LABELS = {
    "scope": "Scope",
    "coverage": "Coverage",
    "period": "Period",
    "spend": "Spend",
    "generated": "Generated",
    "empty_title": "No rows matched this section.",
    "empty_action": "Try a narrower or different filter while keeping the stated scope visible.",
}
INTERNAL_REPORT_HASHES = {
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
    "REDACTED",
}


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise ValueError(f"unsupported schema type {expected}")


def validate_schema_instance(value: Any, schema: dict[str, Any], location: str = "$") -> None:
    if "anyOf" in schema:
        failures = []
        for choice in schema["anyOf"]:
            try:
                validate_schema_instance(value, choice, location)
                break
            except ValueError as exc:
                failures.append(str(exc))
        else:
            raise ValueError(f"{location} does not match any allowed schema: {'; '.join(failures)}")

    expected = schema.get("type")
    if expected is not None:
        choices = expected if isinstance(expected, list) else [expected]
        if not any(type_matches(value, choice) for choice in choices):
            raise ValueError(f"{location} has the wrong type")
    if "enum" in schema and value not in schema["enum"]:
        raise ValueError(f"{location} is not an allowed value")

    if isinstance(value, dict):
        required = schema.get("required", [])
        missing = [name for name in required if name not in value]
        if missing:
            raise ValueError(f"{location} is missing required fields: {', '.join(missing)}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(value) - set(properties))
            if unknown:
                raise ValueError(f"{location} contains unknown fields: {', '.join(unknown)}")
        for key, child in value.items():
            if key in properties:
                validate_schema_instance(child, properties[key], f"{location}.{key}")
    elif isinstance(value, list):
        if len(value) > schema.get("maxItems", len(value)):
            raise ValueError(f"{location} contains too many items")
        item_schema = schema.get("items")
        if item_schema:
            for index, child in enumerate(value):
                validate_schema_instance(child, item_schema, f"{location}[{index}]")
    elif isinstance(value, str):
        if len(value) < schema.get("minLength", 0) or len(value) > schema.get("maxLength", len(value)):
            raise ValueError(f"{location} has an invalid length")
        if schema.get("format") == "date-time":
            try:
                dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError as exc:
                raise ValueError(f"{location} must be an ISO date-time") from exc


def read_payload(source: Path) -> dict[str, Any]:
    raw = source.read_bytes()
    if len(raw) > 1_000_000:
        raise ValueError("input exceeds 1 MB")
    value = json.loads(raw)
    schema = json.loads(SCHEMA_PATH.read_bytes())
    validate_schema_instance(value, schema)
    language = value.get("language", "en")
    if not LANGUAGE_RE.fullmatch(language):
        raise ValueError("language must be a BCP-47 tag")
    reject_internal_report_terms(value)
    return value


def reject_internal_report_terms(value: Any, location: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if contains_internal_report_term(str(key)):
                raise ValueError(f"{location} contains internal public vocabulary")
            reject_internal_report_terms(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_internal_report_terms(child, f"{location}[{index}]")
    elif isinstance(value, str) and contains_internal_report_term(value):
        raise ValueError(f"{location} contains internal public vocabulary")


def contains_internal_report_term(value: str) -> bool:
    candidates = set(re.findall(r"[a-z0-9_.-]+", value.lower()))
    for candidate in tuple(candidates):
        candidates.update(part for part in re.split(r"[_-]+", candidate) if part)
    return any(hashlib.sha256(candidate.encode()).hexdigest() in INTERNAL_REPORT_HASHES for candidate in candidates)


def report_labels(data: dict[str, Any]) -> dict[str, str]:
    labels = dict(REPORT_LABELS)
    labels.update(data.get("labels") or {})
    return labels


def safe_url(raw: str) -> str:
    if any(character.isspace() or ord(character) < 32 for character in raw):
        raise ValueError("links must not contain whitespace or controls")
    parsed = urlparse(raw)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("links must use http or https")
    if parsed.username or parsed.password:
        raise ValueError("links must not contain credentials")
    try:
        port = parsed.port
    except ValueError as exc:
        raise ValueError("links contain an invalid port") from exc
    default_port = 443 if parsed.scheme == "https" else 80
    if port is not None and port != default_port:
        raise ValueError("links must not use a non-default port")
    hostname = parsed.hostname.lower().rstrip(".")
    if hostname == "localhost" or hostname.endswith((".localhost", ".local", ".internal", ".home", ".lan")):
        raise ValueError("private hostnames are not allowed")
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        address = None
    if address is not None:
        raise ValueError("IP-literal link targets are not allowed")
    return quote(raw, safe=":/?#[]@!$&'*+,;=%-._~")


def clean_text(value: Any, limit: int = 10_000) -> str:
    if value is None:
        return "—"
    text = str(value)
    if len(text) > limit:
        raise ValueError("text field exceeds limit")
    return text


def markdown_escape(value: Any) -> str:
    text = clean_text(value)
    for char in ("\\", "`", "*", "_", "[", "]", "<", ">", "|"):
        text = text.replace(char, "\\" + char)
    return text


def render_markdown(data: dict[str, Any]) -> str:
    labels = report_labels(data)
    lines = [f"# {markdown_escape(data['title'])}", "", markdown_escape(data["summary"]), ""]
    lines += [f"**{markdown_escape(labels['scope'])}:** {markdown_escape(data['scope'])}", f"**{markdown_escape(labels['coverage'])}:** {markdown_escape(data['coverage'])}"]
    period = data.get("period") or {}
    if period:
        lines.append(f"**{markdown_escape(period.get('label', labels['period']))}:** {markdown_escape(period.get('value'))}")
    lines.append("")
    for section in data["sections"]:
        if not isinstance(section, dict):
            raise ValueError("section must be an object")
        lines.extend([f"## {markdown_escape(section.get('title', 'Section'))}", ""])
        description = section.get("description")
        if description:
            lines.extend([markdown_escape(description), ""])
        rows = section.get("rows") or []
        if not isinstance(rows, list) or len(rows) > 200:
            raise ValueError("section rows must contain at most 200 items")
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError("row must be an object")
            label = markdown_escape(row.get("label"))
            value = markdown_escape(row.get("value"))
            if row.get("url"):
                url = safe_url(clean_text(row["url"], 2_048))
                value = f"[{value}]({url})"
            lines.append(f"- **{label}:** {value}")
        if not rows:
            lines.append(f"- **{markdown_escape(labels['empty_title'])}** {markdown_escape(labels['empty_action'])}")
        lines.append("")
    lines.extend(["---", f"{markdown_escape(labels['spend'])}: {markdown_escape(data.get('spend', '—'))}", f"{markdown_escape(labels['generated'])}: {markdown_escape(data['generated_at'])}", ""])
    return "\n".join(lines)


def render_html(data: dict[str, Any]) -> str:
    labels = report_labels(data)
    language = data.get("language", "en")
    def esc(value: Any) -> str:
        return html.escape(clean_text(value), quote=True)

    sections: list[str] = []
    for section in data["sections"]:
        rows = section.get("rows") or []
        cards: list[str] = []
        for row in rows:
            value = esc(row.get("value"))
            if row.get("url"):
                url = html.escape(safe_url(clean_text(row["url"], 2_048)), quote=True)
                value = f'<a href="{url}" rel="noreferrer noopener">{value}</a>'
            cards.append(f'<div class="row"><dt>{esc(row.get("label"))}</dt><dd>{value}</dd></div>')
        if not cards:
            cards.append(f'<p class="empty"><strong>{esc(labels["empty_title"])}</strong><br>{esc(labels["empty_action"])}</p>')
        description = f'<p>{esc(section.get("description"))}</p>' if section.get("description") else ""
        sections.append(f'<section><h2>{esc(section.get("title", "Section"))}</h2>{description}<dl>{"".join(cards)}</dl></section>')

    period = data.get("period") or {}
    period_html = ""
    if period:
        period_html = f'<span>{esc(period.get("label", labels["period"]))}: {esc(period.get("value"))}</span>'
    return f"""<!doctype html>
<html lang="{esc(language)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(data['title'])}</title>
<style>
:root{{color-scheme:light dark;font-family:ui-sans-serif,system-ui,sans-serif;line-height:1.5;--surface-sunken:Canvas;--surface-raised:Field;--border:ButtonBorder;--muted:GrayText;--link:LinkText;--focus:Highlight}}
body{{margin:0;background:var(--surface-sunken);color:CanvasText}}main{{max-width:1080px;margin:auto;padding:40px 20px}}
header,section{{background:var(--surface-raised);border:1px solid var(--border);border-radius:16px;padding:24px;margin-bottom:18px}}
h1,h2{{margin-top:0;text-wrap:balance}}.meta{{display:flex;flex-wrap:wrap;gap:10px;color:var(--muted)}}.summary{{font-size:1.08rem;max-width:72ch}}
dl{{margin:0}}.row{{display:grid;grid-template-columns:minmax(140px,1fr) 2fr;gap:16px;padding:10px 0;border-top:1px solid var(--border)}}
dt{{font-weight:650}}dd{{margin:0;overflow-wrap:anywhere}}a{{color:var(--link)}}a:focus-visible{{outline:3px solid var(--focus);outline-offset:3px;border-radius:4px}}.empty{{color:var(--muted);padding:12px 0}}
footer{{color:var(--muted);font-size:.9rem;padding:8px}}
@media(max-width:560px){{main{{padding:18px 12px}}header,section{{padding:18px}}.row{{grid-template-columns:1fr;gap:2px}}}}
@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto!important}}}}
</style>
</head>
<body><main>
<header><h1>{esc(data['title'])}</h1><p class="summary">{esc(data['summary'])}</p><div class="meta"><span>{esc(labels['scope'])}: {esc(data['scope'])}</span><span>{esc(labels['coverage'])}: {esc(data['coverage'])}</span>{period_html}</div></header>
{"".join(sections)}
<footer>{esc(labels['spend'])}: {esc(data.get('spend', '—'))} · {esc(labels['generated'])}: {esc(data['generated_at'])}</footer>
</main></body></html>
"""


def exclusive_write(path: Path, content: str) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--format", choices=sorted(FORMATS), default="both")
    args = parser.parse_args()
    if not SLUG_RE.fullmatch(args.slug):
        raise ValueError("slug must contain lowercase letters, digits and single hyphens")
    if not args.output_dir.is_absolute():
        raise ValueError("output-dir must be absolute")
    run_dir = args.output_dir / args.slug
    run_dir.mkdir(mode=0o700, parents=False, exist_ok=False)
    data = read_payload(args.input.resolve(strict=True))
    if args.format in {"markdown", "both"}:
        exclusive_write(run_dir / "REPORT.md", render_markdown(data))
    if args.format in {"html", "both"}:
        exclusive_write(run_dir / "REPORT.html", render_html(data))
    print(run_dir)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"render_report: {exc}")
