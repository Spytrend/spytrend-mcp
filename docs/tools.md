# Tools

Every tool below is written the same way: what it does, when to use it, when **not** to use it, what
comes back, and an example of the kind of request that leads to it.

You never call these by name. You ask your assistant a question in your own words and it picks the
tool. The reference is here so you know what is possible — and so your assistant has something
precise to work from.

**One word explained before we start.** In this product, a *webmaster* is the company or person
behind a group of ads: one account running many ads across different pages, domains and countries.
The tool names keep the original word; the descriptions do not depend on it.

> Twenty-one advertising tools and the sixteen Startups tools are documented here. Costs are given
> per tool; `get_usage` (tokens) and `estimate_cost` (Startups objects) are free and answer from the
> server itself, so they are the places that cannot go stale.

**Contents**

- Search — [`search_ads`](#search_ads) · [`search_creatives`](#search_creatives) · [`search_advertisers`](#search_advertisers) · [`search_webmasters`](#search_webmasters) · [`search_hubs`](#search_hubs) · [`search_shops`](#search_shops)
- One record in full — [`get_ad`](#get_ad) · [`get_advertiser`](#get_advertiser) · [`get_webmaster`](#get_webmaster) · [`get_creative`](#get_creative) · [`get_shop`](#get_shop) · [`get_media`](#get_media)
- Rankings — [`get_trends`](#get_trends) · [`get_ads_analytics`](#get_ads_analytics)
- Look-alikes — [`find_similar_ads`](#find_similar_ads) · [`find_similar_creatives`](#find_similar_creatives) · [`find_similar_webmasters`](#find_similar_webmasters) · [`get_webmaster_similarity_facets`](#get_webmaster_similarity_facets)
- Folders and balance — [`add_to_favorites`](#add_to_favorites) · [`list_favorites`](#list_favorites) · [`get_usage`](#get_usage)
- Startups — [`search_startups`](#search_startups) · [`get_startup`](#get_startup) · [`compare_startups`](#compare_startups) · [`lookup_startup`](#lookup_startup) · [`enrich_startups`](#enrich_startups) · [`search_funding_rounds`](#search_funding_rounds) · [`search_investors`](#search_investors) · [`get_investor`](#get_investor) · [`search_startup_news`](#search_startup_news) · [`get_startup_ads`](#get_startup_ads) · [`get_startup_ads_growth`](#get_startup_ads_growth) · [`create_company_report`](#create_company_report) · [`retry_company_report`](#retry_company_report) · [`cancel_company_report`](#cancel_company_report) · [`list_company_reports`](#list_company_reports) · [`get_company_report`](#get_company_report) · pricing a call: [`estimate_cost`](#estimate_cost)

---

## Search

### `search_ads`

**What it does.** Searches Meta and TikTok ads by keyword, country, business category, format and
run dates.

**Use when** the user asks what is being advertised in a market, a category or a country, or by a
named brand — or wants to explore a category without knowing a single competitor yet.

**Do not use** when the user already has one ad and wants its full record; that is
[`get_ad`](#get_ad). Or when the question is about the image or video itself rather than the
placement; that is [`search_creatives`](#search_creatives).

**What comes back.** A list of matching ads. For each: its text, the material behind it, who is
advertising, the countries it runs in and the dates it has been running. Enough to decide which ones
are worth opening in full.

**Example request**

> Show me what is being advertised for online language courses in Poland this month.

**Cost.** 1 token per row returned. A page is 20 rows unless you ask for more (200 maximum), and a short page refunds the difference. Ask for five and you pay five.

---

### `search_creatives`

**What it does.** Searches the advertising material itself — the images and videos a person actually
sees — by category, country and format.

**Use when** the question is about the material rather than the placement: which images and videos
are running in a market, and which ones are run again most often.

**Do not use** when the question is about who advertises or where the traffic goes; that is
[`search_ads`](#search_ads) or [`search_advertisers`](#search_advertisers).

**What comes back.** A list of the images and videos running in the market you asked about, with
where each one ran and how often it has been run again.

**Example request**

> What images and videos are running for fitness apps in Italy? Give me the ones that keep getting
> run again.

**Cost.** 1 token per row returned. Downloading a file is a separate step — see [`get_media`](#get_media).

---

### `search_advertisers`

**What it does.** Finds advertisers by name, domain, country or business category.

**Use when** the user names a brand, a company or a site and wants to know whether and how it
advertises.

**Do not use** when the user wants the wider network behind a group of ads rather than one named
advertiser; that is [`search_webmasters`](#search_webmasters).

**What comes back.** Matching advertisers with their pages, the countries they advertise in and the
business categories they fall under.

**Example request**

> Does Acme Furniture advertise anywhere outside the UK? Show me what I can find on them.

**Cost.** 1 token per row returned.

---

### `search_webmasters`

**What it does.** Finds the company or person behind a group of ads — one account running many ads
across pages, domains and countries at once.

**Use when** the user asks who is behind a set of ads, wants the whole operation rather than one
placement, or is mapping who is active in a market.

**Do not use** when a single named brand is the subject; use
[`search_advertisers`](#search_advertisers).

**What comes back.** The accounts running ads in the market you asked about.

**Example request**

> Who is behind the ads for solar panel installation in Spain? I want the accounts behind them, not
> the individual ads.

**Cost.** 1 token per row returned.

---

### `search_hubs`

**What it does.** Explores where advertising sends people, grouped by destination — social
platforms, app stores, marketplaces, shops and other places a link can land.

**Use when** the question is about the destination rather than the ad: which shops or app listings
a market advertises towards, or which profiles on a given platform are being promoted.

**Do not use** to find the ads themselves; that is [`search_ads`](#search_ads). Or when you already
know the domain and want its traffic picture; that is [`search_shops`](#search_shops).

**What comes back.** Asked without a destination, the catalogue itself: what kinds of destination
exist and what they are called. Asked with one, the profiles inside it, filtered by name, business
category and country.

**Example request**

> Which Telegram channels are being advertised for crypto education in Brazil?

**Cost.** The catalogue of destinations is free. Profiles inside a destination cost 1 token per row.

---

### `search_shops`

**What it does.** Looks up domains as traffic surfaces — how much traffic a site gets in a month,
where it comes from, and how much confidence the estimate deserves.

**Use when** you have a domain or want to compare several, and the question is about the site rather
than the advertising that points at it.

**Do not use** for the ads that lead to a site; that is [`search_ads`](#search_ads) with the landing
domain. A row here is a domain, and a domain is not always a company or a product.

**What comes back.** For each domain: a monthly visit estimate, when it was measured, where the
traffic comes from, and flags saying how reliable that estimate is — small sites and sparse data are
marked as such rather than being quietly rounded.

**Example request**

> Compare the traffic of these three online pharmacies and tell me which estimates are solid.

**Cost.** 1 token per row returned.

**A note on the numbers.** Monthly visits are estimates, not measurements taken from the sites themselves. Treat them as a scale, not a meter reading — the reliability flags in the answer are
there to be read.

---

## One record in full

### `get_ad`

**What it does.** Returns the full record of one ad: its text, its image or video, the advertiser,
the countries, the run dates and the page it sends people to.

**Use when** an ad has already been found and the user wants its details, or asks a follow-up about
a specific ad from a previous answer.

**Do not use** to browse or compare; searching many ads is [`search_ads`](#search_ads).

**What comes back.** One ad, complete: the text as written, the material behind it, who is paying
for it, where it runs, how long it has been up and where it sends people.

**Example request**

> Tell me everything about the second ad in that list — where it runs and where it sends people.

**Cost.** 1 token. The ad's material comes with the record.

---

### `get_advertiser`

**What it does.** Returns one advertiser in full: their pages, the countries they advertise in and
the business categories they fall under.

**Use when** the user wants a profile of one named advertiser, or is preparing a summary about a
specific company.

**Do not use** to find advertisers you do not know yet; that is
[`search_advertisers`](#search_advertisers).

**What comes back.** One advertiser, assembled: their pages, which countries their advertising
reaches, and which categories they fall under.

**Example request**

> Give me a profile of that advertiser — which countries, which categories.

**Cost.** 1 token.

---

### `get_webmaster`

**What it does.** Returns everything the company or person behind a group of ads runs: all their
ads, videos, pages, domains, countries and run dates in a single record.

**Use when** the user wants the full picture behind whoever is running the ads, rather than
individual placements. This is the natural follow-up to
[`search_webmasters`](#search_webmasters).

**Do not use** when only one specific ad or one named advertiser is in question.

**What comes back.** The whole body of work in one record: every ad, every video, every page, every
domain, every country and every run date. This is the tool behind *everything a competitor runs* —
you open the account once and the picture is already assembled.

**Example request**

> Take the one running the most ads of those three and show me everything they run — pages,
> domains, countries, and how long each ad has been up.

**Cost.** 1 token, however much the account turns out to run.

---

### `get_creative`

**What it does.** Returns the record of one image or video used in advertising: where it ran and how
often it was run again.

**Use when** the user is working with a specific image or video and wants its record.

**Do not use** to browse material across a market; that is
[`search_creatives`](#search_creatives).

**What comes back.** One image or video: which countries it ran in, the dates, and how many times it
has been put back into rotation.

**Example request**

> That third video — where has it run, and how many times has it been run again?

**Cost.** 1 token.

---

### `get_media`

**What it does.** Downloads the image or video file itself. **Costs 10 credits for an image or video
file, and 1 credit for an ad.**

**Use when** the user explicitly asks to download, save or work with the file.

**Do not use** when the user only wants to know where the material ran — the record from
[`get_creative`](#get_creative) answers that without spending credits.

**What comes back.** The file.

**Example request**

> Download those two videos so I can put them in the deck.

**Cost.** 1 token per ad, 10 per creative. Check your balance first if you are about to work through a batch.

---

### `get_shop`

**What it does.** Returns one domain's full profile.

**Use when** a domain from [`search_shops`](#search_shops) is worth a closer look — its traffic
history, sources and the rest of the record.

**Do not use** to discover domains you do not know yet; that is
[`search_shops`](#search_shops).

**What comes back.** The domain's record: the monthly visit estimate and when it was taken, traffic
sources, history and the reliability flags that go with them.

**Example request**

> Give me the full picture for this shop's domain, including how its traffic moved this year.

**Cost.** 1 token.

---

## Rankings

### `get_trends`

**What it does.** Returns rankings for a country, category or app, including what is newly picking
up.

**Use when** the user asks what is rising, what is new in a category or a country, or wants a
starting point without a specific competitor in mind.

**Do not use** for the history of one known advertiser; that is
[`get_advertiser`](#get_advertiser) or [`get_webmaster`](#get_webmaster).

**What comes back.** Rankings for whatever you scoped it to, with what has recently started picking
up called out separately.

**Example request**

> What is picking up in advertising for meal delivery in France right now?

**Cost.** 1 token per row of rankings returned.

**One thing this is not.** A ranking is a ranking. It says what is running and what is rising. It
does not say what is profitable and it does not recommend what you should run — that call is yours.

---

### `get_ads_analytics`

**What it does.** Takes the same filters you would use to search ads and, instead of the ads,
returns the shape of that selection: how many there are, and how they break down by status,
country, business category, destination domain, advertiser and account.

**Use when** the question is about a market rather than about particular ads — "how much of this
is still running", "which countries does this category go to", "who are the biggest destinations
here". One call answers what would otherwise take pagination and counting by hand.

**Do not use** to list the ads themselves — that is [`search_ads`](#search_ads) with the same
filters. And do not use it on the free tier: this is a Pro-or-higher surface.

**What comes back.** A total, a displayable total, and up to twenty rows per section, each row
tagged with which breakdown it belongs to. Sections say whether they are complete or truncated.

**Two things the numbers mean literally.** A total that comes back empty with a *pending* or
*unavailable* status is **not zero** — it means the count did not settle in time; re-issue the
same call after the wait it names. A real zero arrives as the number 0 with an *exact* status.
And only the status breakdown drops its own filter; every other section describes the same
filtered selection you asked for.

**Example request**

> Of the gambling ads running in Brazil this month, how many are still active, and where do they
> send people?

**Cost.** 1 token per delivered breakdown row. A response that comes back pending or failed
refunds what it reserved.

---

## Look-alikes

These four answer "find me more like this one". They tell you **what** they found and how strong the
match is; how the comparison is made is not part of the answer.

### `find_similar_ads`

**What it does.** Finds other ads carrying the same material as an ad you already have.

**Use when** you have one ad and want to know who else is running the same image or video, and
where.

**Do not use** to search a market from scratch; that is [`search_ads`](#search_ads).

**What comes back.** A list of ads built on the same material, with who runs each one, the countries
and the run dates.

**Example request**

> Who else is running this exact video, and in which countries?

**Cost.** 1 token per row returned.

---

### `find_similar_creatives`

**What it does.** Finds images and videos that look the same as one you already have.

**Use when** you want the family a creative belongs to: the same visual reworked, recut or
re-uploaded.

**Do not use** to browse the material in a market; that is
[`search_creatives`](#search_creatives).

**What comes back.** A list of matching images and videos with where each one ran.

**Example request**

> Find every version of this creative that is running anywhere.

**Cost.** 1 token per row returned.

---

### `find_similar_webmasters`

**What it does.** Finds accounts that advertise like one you already have.

**Use when** you have found one operator worth watching and want the others working the same way.

**Do not use** as a first step — you need a starting account, which comes from
[`search_webmasters`](#search_webmasters).

**What comes back.** A list of accounts with what makes each one comparable.

**Example request**

> This account looks interesting. Who else operates like it?

**Cost.** 1 token per row returned.

---

### `get_webmaster_similarity_facets`

**What it does.** Shows on what grounds accounts can be compared to a given one, and how many
matches each ground would produce — before you ask for the list itself.

**Use when** you want to narrow the comparison before spending anything on results.

**Do not use** to get the accounts themselves; that is
[`find_similar_webmasters`](#find_similar_webmasters).

**What comes back.** The available grounds for comparison with a count against each.

**Example request**

> On what grounds could I compare other accounts to this one, and how many would each give?

**Cost.** Free.

---

## Folders and balance

### `add_to_favorites`

**What it does.** Saves an ad, an image or video, an advertiser or an account to a folder.

**Use when** the user says to keep, save or come back to something later.

**Do not use** as a substitute for returning the answer. Saving is *in addition* to answering, not
instead of it.

**What comes back.** Confirmation of what was saved and where.

**Example request**

> Save the ten most interesting of those to a folder called Q4 research.

**Cost.** 1 token for an ad, 10 for a creative — the same as downloading its material, because saving it fetches it. Saving anything else is free.

---

### `list_favorites`

**What it does.** Returns what is in your folders.

**Use when** the user refers to something they saved earlier, or wants to work through a saved set.

**Do not use** to search the whole platform — folders hold only what was saved.

**What comes back.** The contents of your folders.

**Example request**

> What is in my Q4 research folder? Walk me through it.

**Cost.** Free.

---

### `get_usage`

**What it does.** Shows how many credits are left.

**Use when** the user asks about their limit, or before a large batch of downloads.

**Do not use** before every single call — it is a check, not a routine step.

**What comes back.** Your plan, your balance and what each kind of call costs.

**Example request**

> How many tokens do I have left?

**Cost.** Free. Checking your balance never costs anything.

---

## Startups

The Startups tools work with a catalogue of funded companies: their funding rounds, investors,
revenue and valuation figures, team size, website traffic, news and advertising. They are a
separate product from the advertising tools above.

**Plan.** The Startups tools require the **Startups Business** plan, which is separate from the
advertising plans. The Startups Trial and PRO plans do not include access for AI assistants. Without
Business, the tools do not appear in your assistant, and a call that reaches the server comes back
with a plain refusal that names the plan — a plan matter, not a fault.

**Billing in objects, not tokens.** Startups calls are paid from their own monthly allowance,
counted in *objects*:

- one returned row (a company, a round, an investor, a news item, an ad) — **1 object**;
- one company card — **5 objects**;
- **25,000 objects a month** per subscription, shared by all its seats.

Advertising tokens are never spent on Startups calls, and Startups objects are never spent on
advertising calls. Every Startups response reports `objects_charged` and `objects_remaining`.

**Ask the price first.** Before a card read, a comparison, a batch or a long run of pages, your
assistant calls [`estimate_cost`](#estimate_cost) — free — with the same tool and arguments, and tells
you how many objects the call can take and how many are left. Reading your own company reports is
free and needs no estimate. Ordering a report takes one report from the monthly company-report
allowance, not objects; `estimate_cost` says how many reports are left.

**Limits.** At most 20 results per call. At most 60 Startups calls a minute per subscription. Twenty
or more follow-up pages less than 10 seconds apart pause Startups for 15 minutes. Both refusals say
how long to wait; your assistant should pass that on, not retry in a loop. The full list is in
[docs/limits.md](limits.md#startups-objects).

**How to read the numbers.**

- A missing figure is **unknown, never zero**. A company with no reported revenue has an unknown
  revenue, not a revenue of 0.
- A round amount describes **the whole round**, not one investor's cheque.
- Revenue, ARR and valuation carry a quality label — *reported* (disclosed by the company, a filing or
  the press) or *estimate*. They are different measures and are shown side by side, not merged.
- Website traffic is a monthly estimate, not a measurement.
- Ad launches before and after a funding round are a correlation, not proof that one caused the
  other.
- Team members are public, privacy-filtered records with partial coverage. There are no contacts.

---

### `search_startups`

**What it does.** Searches the catalogue of funded companies by keyword, country, business category,
stage, round type and dates, funding, revenue, ARR and valuation (with their quality label), team
size, website traffic and its growth, paid-traffic share, technologies detected on the website,
growth of ad launches, investor and advertising activity — or by an explicit list of domains.

**Use when** the user wants a list of companies that match a profile: *Series A fintech in Germany
that started advertising*, *AI companies that raised in the last 90 days*, *companies backed by this
investor*.

**Do not use** to open one company in full; that is [`get_startup`](#get_startup). For a company the
search does not return, use [`lookup_startup`](#lookup_startup).

**What comes back.** Company rows with offset paging and `has_more`. `view=facets` returns value
counts for the filters and `view=summary` returns totals with stage and country breakdowns — one
object each, instead of paging through the list. Lists can be sorted, among others, by ARR, last
round date or amount, total funding, team size, ads, Facebook ads over the last 30 days and
active Google ads.

**Example request**

> Find seed and Series A health-tech companies in the UK that raised this year and run ads.

**Cost.** 1 object per returned row; 1 object for facets or a summary.

---

### `get_startup`

**What it does.** Opens one company card by domain: profile, funding rounds, metrics, traffic
estimates, news, deals and advertising history. `include=people` adds public, privacy-filtered team
members; `include=similar` adds similar companies.

**Use when** one company is the subject and the user wants its full record.

**Do not use** to compare several companies at once; that is
[`compare_startups`](#compare_startups). For the company's ads, use
[`get_startup_ads`](#get_startup_ads) with its domain.

**What comes back.** One company card, plus the sections you asked for, each with its own status.

**Example request**

> Give me the full card for example.com — rounds, investors, traffic and team.

**Cost.** 5 objects per card, plus 1 object per included row.

---

### `compare_startups`

**What it does.** Compares **2 to 4 companies** side by side by domain: profile, funding (last
round, total funding, valuation), ARR and revenue with their quality labels, team size, website
traffic and advertising activity, aligned field by field in the order you gave.

**Use when** the user wants several companies set against each other on the same fields.

**Do not use** for a written comparison report; order that with
[`create_company_report`](#create_company_report) and read it with [`get_company_report`](#get_company_report).

**What comes back.** Each value carries a status: *known*, *unknown* (the company card has no such
figure — unknown, never zero) or *card unavailable*. A field names a leader only when at least two
companies have a known number and one of them is strictly the largest. `include_cards=true` also
returns each full company card at no extra cost.

**Example request**

> Compare these three payment startups on funding, revenue, team size and ads: a.com, b.com, c.com.

**Cost.** 5 objects per delivered company card; failed and duplicate domains cost nothing.

---

### `lookup_startup`

**What it does.** Finds a company the catalogue search did not return, by name, domain or website
URL, with an optional country.

**Use when** [`search_startups`](#search_startups) has no row for a company the user is sure exists.

**Do not use** as a general search; it looks for one company.

**What comes back.** A status: *visible* (already in the catalogue — open it with
[`get_startup`](#get_startup)), *found* (a new company, with its row), *collecting* (its profile is
being assembled — try again later), *ambiguous* (a short list of candidates to choose from),
*not found* (re-checked automatically; the answer says when) or *unavailable*. The answer can take
up to about 30 seconds.

**Example request**

> I can't find Acme Robotics in the catalogue. Can you look it up?

**Cost.** 1 object, and only when a found company row is returned. Every other answer is free.

---

### `enrich_startups`

**What it does.** Reads the company cards for a batch of up to 20 domains in one call.

**Use when** the user has a list of companies — a CRM export, a portfolio, a conference list — and
wants the same card for each.

**Do not use** for one company; that is [`get_startup`](#get_startup). It reads the existing
catalogue; it does not start collection, set up alerts or write anywhere.

**What comes back.** One entry per input, in your order, with a status: *ok*, *invalid*,
*not found*, *unavailable* or *allowance exhausted*. Duplicates are recognised and fetched once.
Public team members can be included in the card.

**Example request**

> Here are fifteen domains from our pipeline. Pull funding and team size for each.

**Cost.** 5 objects per delivered company card; failed and duplicate inputs cost nothing.

---

### `search_funding_rounds`

**What it does.** Searches funding rounds by country, business category, round type, minimum amount
and date.

**Use when** the question is about the deals themselves: *who raised a Series B in France last
quarter*.

**Do not use** for the companies' full records; open a company with [`get_startup`](#get_startup) and
an investor with [`get_investor`](#get_investor).

**What comes back.** Round rows. An amount describes the whole round; a missing amount is unknown,
never zero.

**Example request**

> List climate-tech rounds above $10M in Europe since July.

**Cost.** 1 object per returned row.

---

### `search_investors`

**What it does.** Searches investors by name and by the rounds they joined: country, category, round
type, stage, period, amount, and whether they led.

**Use when** the user wants to find who backs a kind of company, or to identify one investor.

**Do not use** for one investor's full record; that is [`get_investor`](#get_investor).

**What comes back.** Investor rows with a key for [`get_investor`](#get_investor). `view=facets` and
`view=summary` describe the filtered investors in one object.

**Example request**

> Which investors led the most seed rounds in Spanish fintech this year?

**Cost.** 1 object per returned row; 1 object for facets or a summary.

---

### `get_investor`

**What it does.** Opens one investor card by key. One optional section can be added: the rounds it
joined, disclosed holdings, funds, related investors and funds, its public team (partial coverage),
the valuation progression of its portfolio, or its funds in public filings and one fund's filing
history.

**Use when** one investor is the subject.

**Do not use** to find investors; that is [`search_investors`](#search_investors).

**What comes back.** The investor card and the section you asked for. Disclosed cheques, portfolio
marks and reported fund returns are measures of their own and are not the same as round totals.

**Example request**

> Show me the last twenty rounds this fund joined, newest first.

**Cost.** 1 object for the card, plus 1 object per returned section row.

---

### `search_startup_news`

**What it does.** Searches startup news — funding, acquisitions, revenue and valuation events — by
keyword, company domain, event type and publication date.

**Use when** the user wants what happened recently around a company or a theme.

**Do not use** for a structured list of rounds; that is
[`search_funding_rounds`](#search_funding_rounds).

**What comes back.** News rows with the event type and the publication date.

**Example request**

> Any acquisition news about example.com this year?

**Cost.** 1 object per returned row.

---

### `get_startup_ads`

**What it does.** Returns the Meta or TikTok ads whose landing page belongs to a catalogue company,
newest first; a domain narrows it to one company.

**Use when** the user wants to see how a funded company advertises.

**Do not use** for advertising research without a catalogue company in mind; that is
[`search_ads`](#search_ads).

**What comes back.** The same ad records as [`search_ads`](#search_ads), paged by cursor. Opening an
ad in full or downloading its material is done with [`get_ad`](#get_ad) and
[`get_media`](#get_media), which are billed in advertising tokens.

**Example request**

> What ads has example.com been running on TikTok?

**Cost.** 1 object per returned ad, from the Startups allowance — no advertising plan is needed to
read these rows, TikTok included.

---

### `get_startup_ads_growth`

**What it does.** Analytics across the catalogue: funding volume over time or by group, ad launches
before and after funding rounds, the companies whose ad launches grew after a round, and investor
activity.

**Use when** the question is about the market rather than one company: *how did funding in AI move
by month*, *do companies launch more ads after a Series A*.

**Do not use** for one company's history; that is [`get_startup`](#get_startup).

**What comes back.** Rows for the metric you chose. A rise in ads after a round is a correlation, not
a cause.

**Example request**

> Which companies grew their ad launches most in the three months after their last round?

**Cost.** 1 object per returned row; the before-and-after view of ad launches is one object.

---

### `create_company_report`

**What it does.** Orders a written research report from the Startups section of spytrend.com: one
domain gives a report on that company, two to four domains give a comparison report. The report is
written in the background; this call returns its id and status straight away.

**Use when** the user asks for a written report or a written comparison, not just the figures.

**Do not use** for a side-by-side table of figures — that is [`compare_startups`](#compare_startups),
which needs no report from the allowance.

**What comes back.** The report id, its status (queued or running at first), the companies, the
objective and period, where it was paid from (the allowance or the balance), and how many reports
remain this month. Ordering the same report again while
the first is still in progress returns the existing one and takes nothing.

**Example request**

> Order a comparison report on example.com and example.org: who is growing faster and why?

**Cost.** 1 report from your monthly company-report allowance (Startups Business: 5 a month, shared
by the team). No Startups objects. When the allowance is used up, the order is refused with the price
of a paid report — 150 balance tokens per company — and your balance. A paid report is ordered only
when you agree to that price: the assistant then repeats the order with `allow_paid`. Without your
consent nothing is ever taken from the balance.

---

### `retry_company_report`

**What it does.** Orders a failed or cancelled report again.

**Use when** a report you own ended as failed or cancelled.

**Do not use** on a report that is queued, running or ready; it comes back unchanged and takes
nothing.

**What comes back.** The same shape as [`create_company_report`](#create_company_report).

**Example request**

> That report failed — try it again.

**Cost.** 1 report from the allowance; beyond it, the same paid-report rule as
[`create_company_report`](#create_company_report).

---

### `cancel_company_report`

**What it does.** Cancels one of your reports that is still queued or running.

**Use when** the user changed their mind or ordered the wrong companies.

**Do not use** on a ready report; there is nothing to cancel.

**What comes back.** The new status and the reports remaining; the cancelled report goes back to the
allowance.

**Example request**

> Cancel the report I just ordered.

**Cost.** Free.

---

### `list_company_reports`

**What it does.** Lists your own company reports from the Startups section of spytrend.com: research
reports for one company or a comparison, with their status (queued, running, ready, failed,
cancelled), and your saved comparisons and briefs.

**Use when** the user refers to a report they already have.

**Do not use** to order a new report; that is [`create_company_report`](#create_company_report).

**What comes back.** Report ids for [`get_company_report`](#get_company_report) and the month's
research-report allowance.

**Example request**

> What company reports do I have for example.com?

**Cost.** Free.

---

### `get_company_report`

**What it does.** Opens one of your company reports by id: its status, its input (companies,
objective, period) and, once it is ready, the content — executive summary, metrics, events,
comparison criteria, investment brief, advertising section and evidence with source links.

**Use when** the user wants to read or discuss a report from the list.

**Do not use** for someone else's report; it is not found.

**What comes back.** The report. Each claim carries a status — reported, company claim, third-party
estimate, derived, unknown or unconfirmed — and a missing figure is unknown, never zero.

**Example request**

> Open my comparison report from last week and summarise the investment brief.

A report you have just ordered has no content until its status is ready; ask again a little later.

**Cost.** Free.

---

### `estimate_cost`

**What it does.** Prices a call before it is made. Pass the tool you are about to call and exactly
its arguments; for a Startups tool it returns the most objects that call can charge and the objects
left in the subscription this month. For `create_company_report` and `retry_company_report` it says
that the call uses 1 of the reports remaining this month, and when the allowance renews; when none
are left, it gives the price of a paid report and your balance.

**Use when** the next Startups call is a card read, a comparison, a batch or a run of pages.

**Do not use** for the free report readers; they cost nothing.

**What comes back.** The upper bound in objects, how it was computed, and what remains. Only
delivered rows and cards are charged; the rest is refunded.

**Example request**

> Before you compare those four companies, tell me what it will cost.

> How many company reports do I have left this month?

**Cost.** Free. It does not run the tool.

---

## If a tool is not doing what you expect

Ask your assistant to tell you which tool it used and what it passed. Most surprises come down to a
question that could be read two ways — "show me their ads" can mean the placements or the images and
videos inside them, and the two live in different tools.

Anything that looks like a genuine fault: <https://spytrend.com/contact/>.
