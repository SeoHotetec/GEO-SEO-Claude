# MCP setup: Google Search Console + GA4

This repo ships independent MCP servers for **Google Search Console** and
**Google Analytics 4**, configured in `.mcp.json` at the repo root.

- **GSC** uses **OAuth** (your own Google Cloud OAuth client) via
  [`google-searchconsole-mcp`](https://www.npmjs.com/package/google-searchconsole-mcp).
- **GA4** uses a **Service Account** via
  [`mcp-server-google-analytics`](https://www.npmjs.com/package/mcp-server-google-analytics).

Both bypass Ahrefs entirely — they call Google's APIs directly with your
own credentials.

## Required env vars (set in the Claude Code remote environment)

Open the environment settings for this repo → Variables, and add:

### GSC (OAuth)

| Variable             | Value                                                            |
| -------------------- | ---------------------------------------------------------------- |
| `GSC_CLIENT_ID`      | `client_id` from your OAuth client JSON                          |
| `GSC_CLIENT_SECRET`  | `client_secret` from your OAuth client JSON                      |
| `GSC_REFRESH_TOKEN`  | Long-lived refresh token (see "Generating the refresh token")    |

### GA4 (Service Account)

| Variable               | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| `GOOGLE_CLIENT_EMAIL`  | `client_email` from the service account JSON        |
| `GOOGLE_PRIVATE_KEY`   | `private_key` from the JSON (keep the `\n` escapes) |
| `GA4_PROPERTY_ID`      | GA4 property ID, e.g. `123456789`                    |

## One-time Google Cloud setup

1. In Google Cloud Console, create or select a project.
2. Enable APIs:
   - **Google Search Console API**
   - **Google Analytics Data API** (GA4)
3. For **GSC**: Credentials → Create credentials → **OAuth client ID** →
   Application type **Desktop app**. Download the JSON (you'll use
   `client_id` and `client_secret`).
4. For **GA4**: create a **Service Account** and download its JSON key.
   In GA4 admin, add the service account email as **Viewer** on the
   property.

## Generating the GSC refresh token (once)

The MCP needs a refresh token so it can authenticate without a browser
each session. Easiest path: **OAuth 2.0 Playground**.

1. Go to <https://developers.google.com/oauthplayground>.
2. Top-right gear → tick **Use your own OAuth credentials** → paste your
   `client_id` and `client_secret`.
3. **Step 1** → in the input box, add scope:
   `https://www.googleapis.com/auth/webmasters.readonly`
4. Click **Authorize APIs**, sign in with the Google account that owns
   the GSC properties, grant consent.
5. **Step 2** → click **Exchange authorization code for tokens**.
6. Copy the **Refresh token** value — this is your `GSC_REFRESH_TOKEN`.

> **Important**: in step 2 of Google Cloud OAuth client setup, add
> `https://developers.google.com/oauthplayground` as an **Authorized
> redirect URI** of your OAuth client, otherwise step 4 above fails.

## Verifying it works

After setting the env vars and starting a fresh session, both `gsc` and
`ga4` servers should appear in the MCP list:

- GSC: `list_sites` → returns the verified properties of the authorized
  account.
- GA4: a basic `runReport` against the configured `GA4_PROPERTY_ID`.

## Notes

- Both MCPs are community-maintained. Pinning a version
  (`google-searchconsole-mcp@x.y.z`) in `.mcp.json` is recommended once a
  version is validated.
- The OAuth refresh token does not expire under normal use, but Google
  may invalidate it if the consent screen status is "Testing" with no
  recent activity, or if the user revokes access. If you start getting
  401s, regenerate it via the same Playground flow.
