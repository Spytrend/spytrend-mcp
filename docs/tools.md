# Tools

Every tool below is written the same way: what it does, when to use it, when **not** to use it, what
comes back, and an example of the kind of request that leads to it.

You never call these by name. You ask your assistant a question in your own words and it picks the
tool. The reference is here so you know what is possible — and so your assistant has something
precise to work from.

**One word explained before we start.** In this product, a *webmaster* is the company or person
behind a group of ads: one account running many ads across different pages, domains and countries.
The tool names keep the original word; the descriptions do not depend on it.

> All twenty-one tools the server exposes are documented here. Costs are given per tool; `get_usage` is
> free and always answers from the server itself, so it is the one place that cannot go stale.

**Contents**

- Search — [`search_ads`](#search_ads) · [`search_creatives`](#search_creatives) · [`search_advertisers`](#search_advertisers) · [`search_webmasters`](#search_webmasters) · [`search_hubs`](#search_hubs) · [`search_shops`](#search_shops)
- One record in full — [`get_ad`](#get_ad) · [`get_advertiser`](#get_advertiser) · [`get_webmaster`](#get_webmaster) · [`get_creative`](#get_creative) · [`get_shop`](#get_shop) · [`get_media`](#get_media)
- Rankings — [`get_trends`](#get_trends) · [`get_ads_analytics`](#get_ads_analytics)
- Look-alikes — [`find_similar_ads`](#find_similar_ads) · [`find_similar_creatives`](#find_similar_creatives) · [`find_similar_webmasters`](#find_similar_webmasters) · [`get_webmaster_similarity_facets`](#get_webmaster_similarity_facets)
- Folders and balance — [`add_to_favorites`](#add_to_favorites) · [`list_favorites`](#list_favorites) · [`get_usage`](#get_usage)

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

## If a tool is not doing what you expect

Ask your assistant to tell you which tool it used and what it passed. Most surprises come down to a
question that could be read two ways — "show me their ads" can mean the placements or the images and
videos inside them, and the two live in different tools.

Anything that looks like a genuine fault: <https://spytrend.com/contact/>.
