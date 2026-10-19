---
name: spytrend-startup-research
description: >-
  Research funded companies with Spytrend Startups data: a company profile with
  funding rounds, revenue and valuation figures, team size, website traffic and
  ads; a side-by-side comparison of 2 to 4 companies; a lookup for a company the
  catalog does not show yet; and ordering or reading the user's own company
  reports. Requires
  the Startups Business plan; billed in Startups objects, priced with the free
  estimate_cost before every paid call. Use when the user names a startup or a
  company domain and wants its funding, investors, traction or ads, or wants
  companies compared. Triggers: "profile this startup", "how much has X
  raised", "compare these startups", "order a company report", "open my company report"; RU «профиль
  стартапа», «сравни стартапы», «закажи отчёт по компании». Not for advertising research without a company
  in mind (use spytrend-vertical-intel) and not for one website's traffic and
  ads alone (use spytrend-website-review).
---

# Spytrend startup research

Read `references/spytrend-contract.md` before making any data call. The rules
below add what is specific to the Startups tools.

## Access and cost

- The Startups tools require the Startups Business plan. The Startups Trial and
  PRO plans do not include AI-agent access. A `startups_mcp_required` refusal is
  a plan matter: tell the user and stop; do not retry.
- Startups calls are billed in Startups objects, not advertising tokens:
  1 returned row = 1 object, a company card = 5 objects. The subscription has a
  monthly allowance shared by all its seats.
- Start with `get_usage` as the connection preflight. It does not show the
  Startups allowance; `estimate_cost` and every Startups response do.
- Before every paid Startups call, call `estimate_cost` (free) with exactly the
  tool name and arguments you are about to send. Tell the user the maximum
  objects it will charge and the objects remaining, and wait for confirmation
  when the user has not already agreed to that spend.
- `list_company_reports`, `get_company_report` and `cancel_company_report` are
  free; they need no estimate.
- `create_company_report` and `retry_company_report` take 1 report from the
  monthly company-report allowance (5 on Business, shared by the team), not
  objects. Call `estimate_cost` first, tell the user "uses 1 of N remaining
  reports" and order only after the user agrees.
- Beyond the allowance a report is paid from the balance (the price comes in
  the estimate). Set `allow_paid=true` only after the user explicitly agrees to
  that price in this conversation; never on your own.
- After each call, report `objects_charged` and `objects_remaining` from the
  response. Sum the charged objects of this run for the spend line.
- At most 20 results per call. Page only when the user asks; never fire pages
  back to back. `startups_rate_limited` and `pagination_paused` carry
  `retry_after_seconds`: report the wait, do not loop.

## Inputs

- `mode` is one of `profile`, `compare`, `lookup`, `reports` or `order_report`.
- `company` is a company name, domain or website URL (profile, lookup, reports).
- `companies` is a comma-separated list of 2 to 4 domains (compare, or a
  comparison report in order_report; one domain in `company` orders a report on
  that company).
- `objective` is the optional question a report should answer (order_report).
- `window_days` is 30, 90 or 365; default 90 (order_report).
- `country` is an optional ISO-2 code that narrows a lookup or a name search.
- `include_people` defaults to `false`. Team members are public,
  privacy-filtered records; never present them as contacts and never guess an
  email or phone number.

## Workflow

### Profile one company

1. A domain or URL goes straight to step 2. A name goes first to
   `search_startups` with `q`, the optional `country` and `limit` 5 (estimate
   first). Present the candidates and let the user pick when more than one
   matches. When nothing matches, follow "Find a company outside the catalog".
2. Estimate, then call `get_startup` with the `domain`. Add `include=["people"]`
   only when `include_people` is `true`, and keep `limit` small.
3. Optional, each after its own estimate and only when the user wants it:
   `search_startup_news` with the `domain` and a small `limit` for recent
   events; `get_startup_ads` with the `domain`, `source` meta or tiktok and a
   small `limit` for the company's ads.

### Compare 2 to 4 companies

1. Normalize the list to 2 to 4 distinct domains; duplicates are compared once.
   Ask the user to cut a longer list.
2. Estimate, then call `compare_startups` with `domains` in the user's order.
   Add `include_cards=true` only when full cards are needed; it costs nothing
   extra.
3. Render field by field in the order of `domains`. Show each value with its
   status: `known`, `unknown` or `card_unavailable`, and the quality label when
   one is present (reported or estimate). Name a leader only where the response
   names `highest`; otherwise say that no company leads on that field.

### Find a company outside the catalog

1. Estimate, then call `lookup_startup` with `q` and the optional `country`.
   The answer can take about 30 seconds.
2. Read `status`:
   - `visible`: the company is already in the catalog under `domain`; open it
     with the profile workflow.
   - `found`: a new company; its row is in `company`.
   - `collecting`: its profile is being assembled; tell the user to retry
     later. Do not poll.
   - `ambiguous`: show the candidates in `options` and ask which one is meant.
   - `not_found`: say so and give `retry_at` when present.
   - `unavailable`: report it; do not retry in a loop.

### Read the user's own company reports

1. Call `list_company_reports`; narrow with `domain`, `kind` or `source` when
   the user names them. Page saved reports with `saved_next_cursor` only on
   request.
2. Call `get_company_report` with the `report_id` and `type` from the list.
3. A report whose status is not ready has no content yet; say which status it
   is in. A report the user does not own is not found.

### Order a company report

1. Call `estimate_cost` with `create_company_report` and the exact arguments
   (`domains`, optional `objective`, `window_days`, `language`). Tell the user it
   uses 1 of the remaining reports and when the allowance renews. If none are
   left, give the paid price and the balance from the estimate and ask whether
   to order a paid report; stop if the user does not agree.
2. After the user agrees, call `create_company_report` (with `allow_paid=true`
   only when the user agreed to the paid price). `already_existed=true`
   means the same report was already in progress; nothing was taken.
3. The report is written in the background. Tell the user its id and status.
   Check it with `get_company_report` (free) when the user asks or after a
   reasonable wait; never poll in a tight loop.
4. When the status is ready, read it as in the previous workflow. On failed,
   offer `retry_company_report` (1 report, estimate first). The user can cancel
   a queued or running report with `cancel_company_report`; it goes back to the
   allowance.
5. `company_reports_exhausted`: the allowance is used up; report the renewal
   date and the paid price. `company_reports_insufficient_balance`: the balance
   cannot pay; report it. `company_reports_daily_limit`: too many orders today; report it, do
   not retry.

## Reading the numbers

- A missing figure is unknown, never zero. Write "unknown"; never fill a gap
  with 0 or with a number from memory.
- A round amount describes the whole round, not one investor's cheque.
- Reported figures and estimates are different measures; keep the quality label
  beside every revenue, ARR or valuation value.
- In a saved report, keep each claim's status (reported, company claim,
  third-party estimate, derived, unknown, unconfirmed) beside the claim.
- Website traffic is a monthly estimate, not a measurement.
- Ads appearing before or after a funding round is a correlation, not proof that
  one caused the other.

## Report

Show the mode, the companies covered, each section's coverage (returned rows,
`has_more`, unknown or unavailable values), and the spend in Startups objects.
A company card is a record of the catalog, not a verdict on the company; give
no investment advice.

Use `references/report-template.md` or the packaged renderer with
`references/report-template.html`; otherwise provide the complete result in
chat.
