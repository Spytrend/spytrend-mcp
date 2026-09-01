# Quickstart — connect in five minutes

Everything you need is on this line:

```
https://mcp.spytrend.com/mcp
```

There is nothing to install and no key to paste. You sign in through the browser with your Spytrend
account — the same one you use on the site. If you do not have one yet, create it at
<https://spytrend.com/> first; the free plan is enough to try the connection.

Pick your client below.

---

## Claude

Works in the Claude desktop app, in the CLI and on the web.

**Step 1.** Open **Settings → Connectors** and choose **Add custom connector**.

**Step 2.** Give the connector a name — `Spytrend` — and paste the endpoint URL into the URL field:

```
https://mcp.spytrend.com/mcp
```

**Step 3.** Confirm. A browser window opens with the Spytrend sign-in. Sign in, allow access, and
the window closes on its own.

**Check it worked.** Ask:

> What advertising tools do you have available right now?

The assistant should now have Spytrend tools available. If it does not, see
[Troubleshooting](#troubleshooting).

---

## ChatGPT

**Step 1.** Open **Settings → Connectors** and add a new connector.

**Step 2.** Paste the endpoint URL:

```
https://mcp.spytrend.com/mcp
```

**Step 3.** Confirm and sign in with your Spytrend account in the window that opens.

**Check it worked.** Ask:

> Using Spytrend, show me what is being advertised for home services in Spain right now.

---

## Cursor

Add the endpoint above as a remote MCP server of type `streamable-http` in Cursor's MCP settings,
then reload. On the next call to a Spytrend tool, a browser window opens for the sign-in.

---

## Codex

Add the endpoint above as a remote MCP server of type `streamable-http` in your Codex
configuration, then sign in through the browser when prompted.

---

## VS Code

Add the endpoint above as a remote MCP server of type `streamable-http` in your MCP configuration,
then reload the window. The sign-in opens in your browser on the next tool call.

---

## Any other client

Anything that speaks **Streamable HTTP** will work. Point it at:

```
https://mcp.spytrend.com/mcp
```

and let it handle the browser sign-in. There is no separate key to issue.

---

## Your opening question

Once you are connected, try one of these. Write them in your own words — the assistant picks the
tools itself.

> I sell running shoes in Germany. Who else is advertising in this space right now, and what are
> they running?

> Show me the ads running for language schools in Brazil, sorted by how long they have been running.

> What is new and picking up in advertising for home services in the UK?

More, with what comes back and how to read it: [the recipes](../examples/).

---

## Troubleshooting

**The assistant does not see any Spytrend tools.**
Restart the client. Most clients read their connector list at startup and will not notice a server
you added while they were running.

**The sign-in window opens and immediately closes, and nothing is connected.**
You are probably signed in to a different Spytrend account in that browser, or to none. Open
<https://spytrend.com/> in the same browser, sign in there, then retry the connection.

**A tool call comes back saying you need to sign in.**
Sign-ins expire. Reconnect the connector; you will not lose anything.

**A call comes back saying the balance is not enough.**
That is a plan matter, not a fault — the assistant should say so rather than retry. Ask it to check
your balance, then either ask for fewer rows or top up at <https://spytrend.com/pricing/>. See
[docs/limits.md](limits.md).

**The client rejects the URL.**
Use the address exactly as it is written on this page, including the `/mcp` at the end and without
a trailing slash.

Still stuck: <https://spytrend.com/contact/>.

---

## Autonomous agents

An AI agent working without a person at the keyboard does not have to wait for anyone to sign up. It
can register itself as a machine client and start sampling the database immediately:

1. `POST https://mcp.spytrend.com/oauth2/register` with a client name and the
   `client_credentials` grant → back come a client id and secret.
2. `POST https://mcp.spytrend.com/oauth2/token` with those credentials, scope `mcp:read` and
   `audience=https://mcp.spytrend.com/mcp` → back comes an access token.
3. Call the endpoint as usual with `Authorization: Bearer <token>`.

**What an unlinked agent gets.** Real data, deliberately narrow: ad and creative search restricted
to the archive, market-level rankings, ten rows per call, no media. Enough to judge whether the
answer is here; not enough to collect in bulk.

**Opening the rest.** A person links the agent to their Spytrend account — either by creating agent
credentials at <https://spytrend.com/settings?tab=ai>, or by claiming a self-registered agent by its
client id. The agent then runs on that account's plan.

A refusal that says the agent must be linked is a plan requirement, **not a server error**. It
should be relayed to the user, not retried and not treated as an outage.

The machine-readable version of all of the above lives at <https://mcp.spytrend.com/llms.txt>.
