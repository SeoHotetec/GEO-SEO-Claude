# MCP setup: Google Search Console + GA4

This repo ships independent MCP servers for **Google Search Console** and
**Google Analytics 4**, configured in `.mcp.json` at the repo root. They run
via `npx` and authenticate with a Google Cloud **service account**.

## Packages used

| MCP  | Package                          | Auth env vars                                          |
| ---- | -------------------------------- | ------------------------------------------------------ |
| GSC  | `mcp-server-gsc`                 | `GOOGLE_APPLICATION_CREDENTIALS` (path to JSON file)   |
| GA4  | `mcp-server-google-analytics`    | `GOOGLE_CLIENT_EMAIL`, `GOOGLE_PRIVATE_KEY`, `GA_PROPERTY_ID` |

## Required env vars (set in the Claude Code remote environment)

Open the environment settings for this repo and add:

| Variable                        | Value                                                                 |
| ------------------------------- | --------------------------------------------------------------------- |
| `GCP_SERVICE_ACCOUNT_JSON`      | Full contents of the service account JSON (single line, quoted)       |
| `GOOGLE_CLIENT_EMAIL`           | `client_email` field from the JSON                                    |
| `GOOGLE_PRIVATE_KEY`            | `private_key` field from the JSON (keep the `\n` sequences)           |
| `GA4_PROPERTY_ID`               | GA4 property ID, e.g. `123456789`                                     |

The `SessionStart` hook (`.claude/hooks/materialize-gcp-credentials.sh`) writes
`GCP_SERVICE_ACCOUNT_JSON` to `/tmp/gcp-service-account.json` at the start of
each session so `mcp-server-gsc` can read it. Nothing sensitive is ever
committed; the `.gitignore` blocks accidental JSON commits.

## Google Cloud setup (one-time)

1. In Google Cloud Console, create or select a project.
2. Enable APIs:
   - **Google Search Console API**
   - **Google Analytics Data API** (GA4)
3. Create a **Service Account** and download its JSON key.
4. Grant access:
   - **GSC**: in Search Console, add the service account email as a user of
     each property you want to query (Restricted is enough for read-only).
   - **GA4**: in the GA4 admin, add the service account email as **Viewer**
     on the property.

## Verifying it works

After setting the env vars and starting a fresh session, the GSC and GA4
servers appear in the MCP list. Quick checks:

- GSC: list sites → should return the verified properties.
- GA4: a basic report on the configured `GA4_PROPERTY_ID`.

## Notes

- The two servers are **completely independent of Ahrefs**. Ahrefs' GSC
  tooling routes through Ahrefs' integration; these MCPs hit Google's APIs
  directly with your own credentials.
- Both packages are community-maintained (Google does not publish official
  MCPs). Pinning a version in `.mcp.json` (`mcp-server-gsc@x.y.z`) is
  recommended once a version is validated.
