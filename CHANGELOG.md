## [2.1.0] — skills pack 1.0.3 — 2026-09-05

### Changed

- `skills/` pack 1.0.3. Skill bodies, the contract, schemas and report templates are
  unchanged since 1.0.2; only the surfaces an assistant uses to pick a skill were rewritten:
  each `SKILL.md` description now states the result, the requests it covers and the
  neighbouring skill to use instead, plus a `when_to_use` field with trigger phrases
  (RU/PT/ES/JA). Codex descriptors (`agents/openai.yaml`) carry new short descriptions and
  default prompts and now allow implicit invocation; the spend guard stays in `contract.md`
  (`get_usage` preflight and confirmation before paid calls).
- 1.0.2 (never published here) fixed four workflow defects found in a full run on the
  production server on 2026-09-04: `spytrend-advertiser-overview` passes a Facebook page id
  as `page_id` (not `advertiser_id`, which takes the internal id and ignored page ids
  silently); `spytrend-keyword-search` bounds free-text analytics with a date window;
  `spytrend-website-review` bounds creative-reuse ranking and no longer presents the two
  reuse counters as part and whole; `spytrend-shop-discovery` explains an empty growth cut
  by snapshot freshness.

# Changelog

All notable changes to this repository and to the published catalogue entry are recorded here.
Versions follow [Semantic Versioning](https://semver.org/) and match the `version` field in
`server.json`.

## [2.1.0] — 2026-09-02

### Added

- `skills/` — six ready-made workflows for Claude Code and Codex (vertical intelligence, advertiser
  overview, webmaster overview, website review, keyword search, shop discovery), the shared contract
  they follow, their input schemas and the report renderer. The same pack is served by the server at
  `/.well-known/agent-skills/index.json` for automatic discovery.
- A Skills section in the README and in `llms.txt`, and a pointer to the server-side connection
  manual for autonomous agents.

### Changed

- **The opening paragraph of the README now states the metering as it is:** every plan connects,
  usage is metered in tokens, one delivered row or record costs one token, and a call that returns
  nothing costs nothing. The previous wording said search and lists were free and credits were spent
  only on downloads, which contradicted `docs/limits.md`, the tool reference and the server itself.
- `server.json` bumped to 2.1.0; the catalogue description now mentions the six workflows.
- The previous catalogue name is no longer spelled out in this changelog.

## [2.0.0] — 2026-08-25

The opening public release of this repository, and a replacement for the catalogue entry that has
been live since June 2026.

### Added

- This repository, as the public home of the Spytrend MCP server: catalogue metadata, setup
  instructions, a tool reference and four recipes.
- `server.json` for the official MCP registry, under the name `com.spytrend/spytrend`.
- `llms.txt` — a short machine-readable map of the connection for AI assistants.
- `docs/quickstart.md` — connecting in five minutes, written up per client: Claude, ChatGPT,
  Cursor, Codex and VS Code.
- `docs/tools.md` — every documented tool with what it does, when to use it, when not to use it,
  what comes back and an example request.
- `docs/limits.md` — what each call costs in tokens, what is free, and what the assistant sees when
  the balance runs out.
- `examples/` — four recipes written as plain-language requests.
- `SECURITY.md` — how to report a vulnerability privately.
- MIT licence.

### Changed

- **The catalogue entry was replaced.** Registry names are permanent, so this release is published
  under a new name rather than as a rename of the June 2026 entry.
- **Both advertising sources are now named.** The June entry mentioned Meta only; the connection
  covers Meta and TikTok.
- **The description was rewritten** to match the current positioning: Spytrend is an advertising
  analytics platform.

### Deprecated

- The June 2026 catalogue entry under its previous name — both versions, 1.0.0 of 23 June 2026 and
  1.1.0 of 23 August 2026 — has been removed from the registry in favour of this release. Removal
  rather than deprecation was not a preference: the registry binds one endpoint URL to one server,
  and marking the old entry deprecated does not release that binding, so the new entry could not be
  published while the old one stood. There was no repository behind it; it existed only as a
  registry record. Anyone still pointed at it should move to `com.spytrend/spytrend`; the endpoint
  URL has not changed.

### Notes

- The endpoint `https://mcp.spytrend.com/mcp` is unchanged. Nothing in this release requires an
  existing user to reconnect.
- All twenty-one tools the server exposes are documented here.
- Usage is metered in tokens from a single balance, and you pay for delivered results only. The
  authoritative numbers always come from `get_usage`, which is free and answers from the server.

[2.0.0]: https://github.com/Spytrend/spytrend-mcp/releases/tag/v2.0.0
