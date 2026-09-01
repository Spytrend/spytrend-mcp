# Security

## Reporting a vulnerability

If you have found a security problem in the Spytrend MCP server, the connection endpoint, or
anything in this repository, please report it privately.

**Do not open a public issue.** A public issue tells everyone about the problem before we have a
fix in place.

Two ways to reach us, either is fine:

- **Email:** support@spytrend.com — mark the subject line `SECURITY`
- **GitHub:** open a private security advisory on this repository
  (*Security → Report a vulnerability*)

## What to include

The more of this you can give us, the faster we can act:

- What the problem is, in one or two sentences
- The steps to reproduce it, or a request that shows it
- What an attacker could do with it
- Anything that helps us confirm it: timestamps, request identifiers, screenshots

Please do not include other people's personal data in your report.

## What happens next

| Stage | Target |
|---|---|
| We confirm we received your report | 5 business days |
| We tell you whether we could reproduce it, and what we plan to do | 15 business days |

While a fix is in progress we will keep you informed, without committing to a fixed interval —
we would rather write to you when there is something to say than promise a cadence we cannot hold.

If you would like credit for the report, say so and tell us the name to use. We will name you when
we announce the fix, unless you ask us not to.

## Scope

**In scope**

- `https://mcp.spytrend.com` — the connection endpoint
- The sign-in flow used by the connection
- The contents of this repository

**Out of scope**

- Findings that need physical access to a customer's device
- Reports produced by an automated scanner with nothing to show that the finding is real
- Missing hardening measures with no working attack behind them
- Problems in third-party services we do not run

For anything about the rest of the platform, use the same address — we will route it internally.

## Please do not

- Run load or denial-of-service tests against the endpoint
- Access, change or download data belonging to other users
- Keep any data you come across; tell us instead, and delete your copy

Report in good faith, stay within the boundaries above, and we will not pursue you for the research.
