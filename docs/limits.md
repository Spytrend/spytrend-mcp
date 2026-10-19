# Limits, tokens and plans

## The short version

Usage is metered in **tokens**, from a single balance. **You pay for results, not for asking:** a
call that returns nothing costs nothing, and a page shorter than you asked for refunds the
difference automatically.

One delivered row or record costs **1 token**. Downloading material costs **1** for an ad and **10**
for a creative. TikTok rows cost **100**. Checking your balance is **free**.

The free Starter plan comes with **500 tokens that do not expire**. Every paid plan comes with
**40,000 a month**.

The Startups tools are counted separately, in **objects** — 1 per row, 5 per company card, 25,000 a
month on the Startups Business plan. See [Startups objects](#startups-objects).

---

## What costs what

| Action | Cost |
|---|---|
| A row of search results — ads, creatives, advertisers, accounts, destinations, shops | 1 token per row |
| A row of rankings | 1 token per row |
| One advertiser, account, creative, destination or shop opened in full | 1 token |
| One ad opened in full (it brings the material with it) | 1 token |
| One multilang-upload ad opened in full (`get_ad`) or its media downloaded (`get_media`) | 50 tokens per ad, per new call |
| Downloading an image or video file | 1 per ad · 10 per creative |
| Saving an ad to a folder · saving a creative | 1 · 10 |
| A row from the TikTok corpus (`source=tiktok`, Pro and above) | 100 tokens |
| Checking your balance | Free |
| Listing your folders | Free |
| The catalogue of destinations, and asking on what grounds two accounts look alike | Free |

**Opening a multilang-upload ad costs 50 tokens, not 1.** The 50 tokens are per ad, per new call, and
include the primary creative and all available slides (not 50 per slide); an ordinary ad opened in full
stays at 1 token. If the selected primary media is unavailable, that is not charged. Search rows show
the opening price (`opening_price`) before you open an ad.

**Page size is the thing to watch.** A search returns 20 rows unless you ask for more, and never
more than 200. Twenty rows is twenty tokens — so a plan of 40,000 is roughly two thousand ordinary
searches. If you only need a handful, say so: *"show me the top five"* costs five.

**You are not charged for an empty answer.** Tokens are reserved when the call starts and the
unused part is returned the moment the answer is assembled. A search that matches nothing is free.

---

## Tokens by plan

| Plan | Tokens |
|---|---|
| Starter (free) | 500, and they do not expire |
| Every paid plan | 40,000 per month |
| Enterprise | Set with support |

The connection works on every plan, including the free one.

**One boundary to know about on the free plan.** Results there are limited to the archive: you will
not see advertising from the last 90 days. Every response says so when it applies. This is the same
boundary as the free tier on the site, and it is what the paid plans lift — not the number of
tokens alone.

Your assistant can always ask for the exact numbers — the answer comes from the server, not from
this page:

> How many tokens do I have left, and what does each call cost?

Current pricing: <https://spytrend.com/pricing/?utm_source=github&utm_medium=repo&utm_campaign=mcp-launch>

---

## Startups objects

The Startups tools (see [the tool reference](tools.md#startups)) are a separate product with a
separate allowance. They need the **Startups Business** plan; the Startups Trial and PRO plans do not
include access for AI assistants. They are counted in **objects**, not tokens: a Startups call never
spends tokens, and an advertising call never spends objects.

| Action | Cost |
|---|---|
| A returned row — a company, a round, an investor, a news item, an ad of a catalogue company | 1 object |
| A facets or summary view of a search | 1 object |
| One company card (`get_startup`, each card in `compare_startups` and `enrich_startups`) | 5 objects |
| A row of an extra section on a card (team, similar companies, an investor's rounds and so on) | 1 object |
| One investor card | 1 object |
| `lookup_startup` that returns a found company | 1 object; every other answer is free |
| Ordering a company report (`create_company_report`; `retry_company_report` on a failed or cancelled report) | 1 report from the monthly company-report allowance, no objects |
| A report beyond the allowance, only with your consent (`allow_paid`) | 150 balance tokens per company in the report |
| Cancelling a queued or running report (`cancel_company_report`) | Free; the report goes back to the allowance |
| Reading your own company reports (`list_company_reports`, `get_company_report`) | Free |
| Asking the price of a call (`estimate_cost`) | Free |

| Limit | Value |
|---|---|
| Objects per month | 25,000 per subscription, shared by all its seats |
| Results per call | At most 20 (`enrich_startups`: up to 20 domains; `compare_startups`: 2 to 4) |
| Calls per minute | At most 60 Startups calls per subscription |
| Paging | Twenty or more follow-up pages less than 10 seconds apart pause Startups for 15 minutes |
| Company reports | 5 a month on Startups Business, shared by the team; renews on the 1st (UTC). When none are left the order is refused (`company_reports_exhausted`) with the price of a paid report; it is paid from the balance only with your consent (`company_reports_insufficient_balance` when the balance is too low). At most 10 orders a day per user (`company_reports_daily_limit`) |

**Ask the price before a paid call.** `estimate_cost` takes the tool and exactly its arguments and
answers with the most objects that call can charge and the objects left this month. For a list it
is an upper bound: only delivered rows and cards are charged, the rest is refunded. Every Startups
response also reports `objects_charged` and `objects_remaining`. `get_usage` reports tokens, not
Startups objects.

---

## When something comes back as an error

Business problems come back to your assistant as a tool error with a clear message, not as a
connection failure — so the assistant can explain what happened and what to do next, rather than
just saying the call failed.

| What happened | What you see | What to do |
|---|---|---|
| You are not signed in, or the sign-in has expired | The assistant says it needs you to sign in again | Reconnect the connector in your client. Nothing is lost |
| Your balance has run out | The assistant tells you the balance is not enough and what the call would have cost | Top up at <https://spytrend.com/pricing/?utm_source=github&utm_medium=repo&utm_campaign=mcp-launch>, or ask for fewer rows |
| Nothing matched | The assistant says there is nothing for that request | Widen it: fewer filters, a broader category, a longer date range |
| The request could not be understood | The assistant says a value was not valid and which one | Rephrase the country or category and ask again |
| The Startups tools are not on your plan | The assistant says the Startups Business plan is required | Business is a separate plan from the advertising plans; questions: <https://spytrend.com/contact/> |
| The month's Startups objects are used up | The assistant says the allowance is exhausted | Wait for the next month, or ask for fewer rows and cards |
| Too many Startups calls or pages too fast | The assistant says to wait, and for how long | Wait the time it names; do not retry in a loop |

Note the second row: a refusal for lack of balance is a plan matter, not a fault. Your assistant
should say so and offer to continue with fewer rows — not retry the same call.

---

## Still stuck

Questions about your balance, your plan or your account: <https://spytrend.com/contact/>

Connection problems: [the troubleshooting section of the quickstart](quickstart.md#troubleshooting).
