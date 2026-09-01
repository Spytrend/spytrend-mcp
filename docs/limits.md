# Limits, tokens and plans

## The short version

Usage is metered in **tokens**, from a single balance. **You pay for results, not for asking:** a
call that returns nothing costs nothing, and a page shorter than you asked for refunds the
difference automatically.

One delivered row or record costs **1 token**. Downloading material costs **1** for an ad and **10**
for a creative. TikTok rows cost **100**. Checking your balance is **free**.

The free Starter plan comes with **500 tokens that do not expire**. Every paid plan comes with
**40,000 a month**.

---

## What costs what

| Action | Cost |
|---|---|
| A row of search results — ads, creatives, advertisers, accounts, destinations, shops | 1 token per row |
| A row of rankings | 1 token per row |
| One advertiser, account, creative, destination or shop opened in full | 1 token |
| One ad opened in full (it brings the material with it) | 1 token |
| Downloading an image or video file | 1 per ad · 10 per creative |
| Saving an ad to a folder · saving a creative | 1 · 10 |
| A row from the TikTok corpus (`source=tiktok`, Pro and above) | 100 tokens |
| Checking your balance | Free |
| Listing your folders | Free |
| The catalogue of destinations, and asking on what grounds two accounts look alike | Free |

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

Current pricing: <https://spytrend.com/pricing/>

---

## When something comes back as an error

Business problems come back to your assistant as a tool error with a clear message, not as a
connection failure — so the assistant can explain what happened and what to do next, rather than
just saying the call failed.

| What happened | What you see | What to do |
|---|---|---|
| You are not signed in, or the sign-in has expired | The assistant says it needs you to sign in again | Reconnect the connector in your client. Nothing is lost |
| Your balance has run out | The assistant tells you the balance is not enough and what the call would have cost | Top up at <https://spytrend.com/pricing/>, or ask for fewer rows |
| Nothing matched | The assistant says there is nothing for that request | Widen it: fewer filters, a broader category, a longer date range |
| The request could not be understood | The assistant says a value was not valid and which one | Rephrase the country or category and ask again |

Note the second row: a refusal for lack of balance is a plan matter, not a fault. Your assistant
should say so and offer to continue with fewer rows — not retry the same call.

---

## Still stuck

Questions about your balance, your plan or your account: <https://spytrend.com/contact/>

Connection problems: [the troubleshooting section of the quickstart](quickstart.md#troubleshooting).
