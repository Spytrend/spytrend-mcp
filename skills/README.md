# Spytrend skills

Six ready-made workflows for AI assistants that are connected to the Spytrend MCP server. A skill is
a plain folder: `SKILL.md` tells the assistant when the workflow applies and how to run it, `agents/`
carries the Codex descriptor, `references/` holds the report template. The assistant reads the skill,
decides which tools to call, and renders a report you can send on.

| Skill | Ask it when you want to |
|---|---|
| `spytrend-vertical-intel` | map one advertising vertical in one market: who leads, which networks run it, what is being reused and launched |
| `spytrend-advertiser-overview` | profile a single advertiser: pages, countries, categories, what it runs now |
| `spytrend-webmaster-overview` | see everything the account behind a group of ads runs, across pages, domains and countries |
| `spytrend-website-review` | review a website as a traffic surface: who sends traffic to it and how it is advertised |
| `spytrend-keyword-search` | find what is advertised for a keyword in a market and read the result as a report |
| `spytrend-shop-discovery` | discover shops in a niche and market with their traffic and advertising signals |

## Install

**Claude Code (plugin, one command):**

```text
/plugin marketplace add Spytrend/spytrend-mcp
/plugin install spytrend-mcp-skills@spytrend-mcp
```

**Any assistant via the skills installer** (Claude Code, Codex, Cursor, Copilot, Gemini CLI and 70+ more):

```bash
npx skills add Spytrend/spytrend-mcp
```

**Claude Code.** Copy the skill folders into your skills directory and start a new session:

```bash
cp -R skills/spytrend-* ~/.claude/skills/
```

**Codex.** Each folder carries `agents/openai.yaml`; point Codex at the folder or copy it into your
Codex skills directory.

**Automatic discovery.** The server publishes the same pack at
`https://mcp.spytrend.com/.well-known/agent-skills/index.json`; assistants that read that index pick
the skills up without a copy step.

## What every skill follows

[`contract.md`](contract.md) is the shared contract: how arguments are read, how cost is checked with
`get_usage` before anything is spent, what a report must contain and how it is rendered
(`scripts/render_report.py`, templates under each skill's `references/`). `manifest.json` lists the
skills, the tools each one calls and the input schema (`schemas/`) it validates its arguments against.

The live tool list and the fields each call returns are authoritative when they differ from a cached
client description — every skill says so and is written to re-check rather than assume.
