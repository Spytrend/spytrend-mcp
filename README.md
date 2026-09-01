# Spytrend MCP Server

[![Claude](https://img.shields.io/badge/Claude-Set%20up-1f1f1f?style=flat-square)](docs/quickstart.md#claude)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-Set%20up-1f1f1f?style=flat-square)](docs/quickstart.md#chatgpt)
[![Cursor](https://img.shields.io/badge/Cursor-Set%20up-1f1f1f?style=flat-square)](docs/quickstart.md#cursor)
[![VS Code](https://img.shields.io/badge/VS%20Code-Set%20up-1f1f1f?style=flat-square)](docs/quickstart.md#vs-code)

**Spytrend is an advertising analytics platform.** This repository is the official home of its MCP
server: one URL, a browser sign-in, and your AI assistant works with Meta and TikTok advertising
data directly — ads, the images and videos behind them, advertisers, and whoever is running them.
There is nothing to install and no key to paste: the server runs on our side and you sign in with
your Spytrend account, the same one you use on the site. The connection works on every plan,
including the free one; usage is metered in tokens, and you pay for results, not for asking — a call
that returns nothing costs nothing. One ad is a single frame. Here you see everything a competitor
runs.

---

## What this repository is

This repository holds the public catalogue metadata for a server we host (see `server.json`), plus
setup instructions and recipes. The server itself is part of the Spytrend platform and its source
is not open. There is no package here to download and no code to run — connecting is a URL and a
sign-in button.

---

## Connect

**Endpoint**

```
https://mcp.spytrend.com/mcp
```

**Sign-in:** your Spytrend account, in the browser. No API key, no token to paste.

**Where to find it in your account:** Settings → AI / MCP, or the connection page at
<https://spytrend.com/mcp/>.

Three steps, whichever client you use:

1. Open your client's connector settings.
2. Add a remote MCP server and give it the URL above.
3. Sign in when the browser window opens, and start asking.

Per-client instructions: **[docs/quickstart.md](docs/quickstart.md)**.

<details>
<summary><b>Claude</b> — desktop, CLI and web</summary>

Add a custom connector in Settings → Connectors, paste the endpoint URL, and complete the sign-in
in the browser window that opens. Full walkthrough: [docs/quickstart.md#claude](docs/quickstart.md#claude).
</details>

<details>
<summary><b>ChatGPT</b></summary>

Add the endpoint as a connector in Settings, then sign in with your Spytrend account.
Full walkthrough: [docs/quickstart.md#chatgpt](docs/quickstart.md#chatgpt).
</details>

<details>
<summary><b>Cursor · Codex · VS Code</b></summary>

Add the endpoint above as a remote MCP server of type `streamable-http`, then sign in through the
browser when prompted. Full walkthrough: [docs/quickstart.md](docs/quickstart.md).
</details>

Any client that speaks Streamable HTTP will work — the four above are simply the ones we have
written up.

---

## What you get

**Search.** Ask what is being advertised in a market, a category or a country — by keyword, by
business category, by format, by run dates. Search the advertising material itself, too: the images
and videos a person actually sees.

**One record, in full.** Open a single ad, an advertiser, or the account behind a group of ads, and
get the whole record: the text, the material, the pages, the domains, the countries, the run dates.

**Rankings.** See what is newly picking up in a country, a category or an app — a starting point
when you have no specific competitor in mind.

**Folders and balance.** Save what you find to a folder and pull it back later. Check your balance,
for free, at any time.

**Autonomous agents.** An agent can register itself and start sampling the database before anyone
signs up: archive results, market-level rankings, ten rows a call, no media. Linking it to a
Spytrend account opens the rest. See [docs/quickstart.md](docs/quickstart.md#autonomous-agents).

---

## Everything a competitor runs

One ad is a single frame. Here you see the whole body of work: every ad, every video, every page,
every domain, every country and every run date, gathered into one record. Open the account behind
the advertising once and the whole picture is already assembled — you are not clicking through tabs
building it yourself.

Most services answer one question: *show me this ad.* This one answers a different question:
*who is running it, and what else are they running?*

---

## Tools

| Tool | What it does | Cost |
|---|---|---|
| `search_ads` | Search Meta and TikTok ads by keyword, country, business category, format and run dates | 1 token per row returned |
| `search_creatives` | Search the advertising material itself — the images and videos a person actually sees | 1 token per row returned |
| `search_advertisers` | Find advertisers by name, domain, country or business category | 1 token per row returned |
| `search_webmasters` | Find the company or person behind a group of ads — one account running many ads across pages, domains and countries | 1 token per row returned |
| `search_hubs` | Explore where advertising sends people, grouped by destination: social platforms, app stores, marketplaces, shops | Catalogue of destinations: free. Profiles inside one: 1 token per row |
| `search_shops` | Look up a domain as a traffic surface, with monthly visit estimates and how confident each estimate is | 1 token per row returned |
| `get_ad` | Return the full record of one ad: text, material, advertiser, countries, run dates, destination page | 1 token |
| `get_advertiser` | Return one advertiser in full: pages, countries, business categories | 1 token |
| `get_webmaster` | Return everything the account behind a group of ads runs, in a single record | 1 token |
| `get_creative` | Return the record of one image or video: where it ran and how often it was run again | 1 token |
| `get_shop` | Return one domain's full profile | 1 token |
| `get_media` | Download the image or video file itself | 1 token per ad · 10 per creative |
| `get_trends` | Return rankings for a country, category or app, including what is newly picking up | 1 token per row returned |
| `get_ads_analytics` | Return the shape of a selection of ads instead of the ads: how many, and how they break down by status, country, business category, destination and advertiser | Pro and above · 1 token per breakdown row |
| `find_similar_ads` | Find ads that carry the same material as one you already have | 1 token per row returned |
| `find_similar_creatives` | Find images and videos that look the same as one you already have | 1 token per row returned |
| `find_similar_webmasters` | Find accounts that advertise like one you already have | 1 token per row returned |
| `get_webmaster_similarity_facets` | Show on which grounds two accounts look alike, before you ask for the list | Free |
| `add_to_favorites` | Save an ad, an image or video, an advertiser, a destination or an account to a folder | Ads 1 token · creatives 10 · everything else free |
| `list_favorites` | Return what is in your folders | Free |
| `get_usage` | Show your plan, your balance and what each call costs | Free |

> A page returns 20 rows unless you ask for more, and never more than 200. You are charged for rows
> actually delivered — a short page refunds the difference automatically. The TikTok corpus
> (`source=tiktok`, Pro plan and above) is priced separately at 100 tokens per delivered row.

Each tool with its *use when* / *do not use* guidance, its return shape and an example request:
**[docs/tools.md](docs/tools.md)**.

**One word explained.** In this product, a *webmaster* is the company or person behind a group of
ads: one account running many ads across different pages, domains and countries. The tool names keep
the original word; the descriptions do not depend on it.

---

## Skills

Six ready-made workflows for Claude Code and Codex live in [skills/](skills/): map a vertical,
profile an advertiser or the account behind a group of ads, review a website, search by keyword,
discover shops. Each skill is a plain folder — copy it into your assistant's skills directory and ask
in plain language; the skill decides which tools to call and renders a report. Install steps and
the shared contract: [skills/README.md](skills/README.md).

---

## Recipes

These are the things people ask their assistant on day one. Type the request in your own words — the
assistant picks the tools.

| Recipe | What you ask for |
|---|---|
| [Find who else is advertising in your market](examples/find-competitors.md) | Who is advertising in your space right now, and what are they running |
| [Match to a business type](examples/by-business-type.md) | Advertising from businesses like yours — no competitor names needed |
| [Top ads in one market](examples/top-of-niche.md) | What is running in a category, sorted by how long it has been up |
| [What's running right now in an industry](examples/running-now.md) | What is new and picking up, and what has been running for a while |

---

## Credits and plans

Usage is metered in **tokens**, from one balance. **You pay for results, not for asking:** a call
that returns nothing costs nothing, and a page shorter than you asked for refunds the difference.

- One delivered row or record — **1 token**. That covers a row of search results, a row of rankings,
  and an advertiser, account, destination or creative opened in full.
- Downloading the material itself — **1 token** for an ad, **10** for a creative.
- The TikTok corpus (`source=tiktok`, Pro and above) — **100 tokens** per delivered row.
- Checking your balance, listing your folders, and the catalogue of destinations — **free**.

The free Starter plan comes with **500 tokens, and they do not expire**. Every paid plan comes with
**40,000 tokens a month** — about 2,000 default-sized searches. Enterprise limits are set with
support.

The connection works on every plan, including the free one. **On the free Starter plan results are
limited to the archive — nothing from the last 90 days.** Fresh advertising is what the paid plans
provide; it is the same boundary as the free tier on the site. Your assistant can always ask
`get_usage` — it is free and it answers from the server itself. Current pricing:
<https://spytrend.com/pricing/>

Details, along with what the assistant sees when the balance runs out:
**[docs/limits.md](docs/limits.md)**.

---

## Documentation

| File | What is in it |
|---|---|
| [docs/quickstart.md](docs/quickstart.md) | Connecting in five minutes, per client |
| [docs/tools.md](docs/tools.md) | Every tool: what it does, when to use it, when not to, what comes back |
| [docs/limits.md](docs/limits.md) | Credits, limits, plans, and what an error looks like |
| [examples/](examples/) | Four recipes: what to ask, what comes back, how to read it |
| [skills/](skills/) | Six ready-made workflows for Claude Code and Codex, with install steps and the shared contract |
| `server.json` | Catalogue metadata, published to the official MCP registry |
| `llms.txt` | A short machine-readable map of this connection for AI assistants |

---

## Support

Questions about connecting, access or your account: <https://spytrend.com/contact/>

Something wrong in this repository — a broken link, an instruction that does not match what you see
on screen: open an issue.

Security reports go through a separate route, never through issues: see [SECURITY.md](SECURITY.md).

---

## License

MIT — see [LICENSE](LICENSE). The licence covers the contents of this repository: documentation,
metadata and examples. The server itself is part of the Spytrend platform.
