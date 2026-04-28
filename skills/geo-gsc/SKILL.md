# geo-gsc — Google Search Console Integration

Manage and query Google Search Console properties directly from Claude Code.

## Commands

| Command | Description |
|---------|-------------|
| `/geo gsc properties` | List all GSC properties connected to your account |
| `/geo gsc setup` | Show OAuth2 setup instructions |
| `/geo gsc auth` | Re-authenticate (clear saved token and re-run OAuth flow) |

---

## When this skill is invoked

### `/geo gsc properties`

Run the properties script and display results:

```bash
python3 ~/.claude/skills/geo/scripts/gsc_properties.py
```

If the script exits with an error mentioning missing `client_secrets.json`, show
the setup instructions and tell the user to run `/geo gsc setup`.

If the script exits with an import error, tell the user to install dependencies:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

After a successful listing, summarise the results:
- Total number of properties found
- List each property URL with its permission level
- Highlight any properties where permission is `siteOwner` (full control)

### `/geo gsc setup`

Run:

```bash
python3 ~/.claude/skills/geo/scripts/gsc_properties.py --setup
```

Then walk the user through the steps displayed, offering to open relevant URLs
in the browser if possible.

### `/geo gsc auth`

Run:

```bash
python3 ~/.claude/skills/geo/scripts/gsc_properties.py --auth
```

Then immediately run the properties list again so the user can confirm the new
authentication works.

---

## Authentication flow

Credentials are stored at:

```
~/.geo-seo/gsc/client_secrets.json   ← user provides this (OAuth desktop app)
~/.geo-seo/gsc/token.json            ← auto-created after first auth
```

The first run opens a browser window for Google OAuth consent. Subsequent runs
reuse the stored token and refresh it silently when expired.

---

## Error handling

| Error | Action |
|-------|--------|
| `client_secrets.json not found` | Show setup instructions |
| Import error (missing packages) | Show `pip install` command |
| `invalid_grant` or token error | Suggest running `/geo gsc auth` |
| No properties returned | Confirm account has GSC properties at search.google.com/search-console |
