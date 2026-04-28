#!/usr/bin/env python3
"""
List Google Search Console properties accessible via OAuth2 API.

Usage:
    python3 gsc_properties.py                  # list properties (table format)
    python3 gsc_properties.py --json           # output raw JSON
    python3 gsc_properties.py --auth           # re-authenticate (delete stored token)
    python3 gsc_properties.py --setup          # show setup instructions

Authentication:
    1. Place client_secrets.json at ~/.geo-seo/gsc/client_secrets.json
    2. First run opens a browser to authorise access
    3. Token is stored at ~/.geo-seo/gsc/token.json for reuse
"""

import argparse
import json
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
CONFIG_DIR = Path.home() / ".geo-seo" / "gsc"
TOKEN_FILE = CONFIG_DIR / "token.json"
SECRETS_FILE = CONFIG_DIR / "client_secrets.json"

PERMISSION_LABELS = {
    "siteOwner": "Owner",
    "siteFullUser": "Full User",
    "siteRestrictedUser": "Restricted User",
    "siteUnverifiedUser": "Unverified",
}

SETUP_GUIDE = """
GSC API Setup Instructions
===========================

1. Go to Google Cloud Console:
   https://console.cloud.google.com/

2. Create or select a project.

3. Enable the Search Console API:
   APIs & Services → Library → "Google Search Console API" → Enable

4. Create OAuth 2.0 credentials:
   APIs & Services → Credentials → Create Credentials → OAuth client ID
   Application type: Desktop app
   Download the JSON file.

5. Place the downloaded file at:
   {secrets_path}

6. Run this script again to authenticate.
""".format(secrets_path=SECRETS_FILE)


def _require_google_libs():
    try:
        from google.oauth2.credentials import Credentials  # noqa: F401
        from google.auth.transport.requests import Request  # noqa: F401
        from google_auth_oauthlib.flow import InstalledAppFlow  # noqa: F401
        from googleapiclient.discovery import build  # noqa: F401
    except ImportError:
        print(
            "ERROR: Required Google API packages not installed.\n"
            "Run: pip install google-auth google-auth-oauthlib "
            "google-auth-httplib2 google-api-python-client"
        )
        sys.exit(1)


def _get_credentials():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not SECRETS_FILE.exists():
                print(f"ERROR: client_secrets.json not found.\n{SETUP_GUIDE}")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(str(SECRETS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)

        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json())

    return creds


def fetch_properties():
    from googleapiclient.discovery import build

    creds = _get_credentials()
    service = build("searchconsole", "v1", credentials=creds)
    response = service.sites().list().execute()
    return response.get("siteEntry", [])


def print_table(sites):
    if not sites:
        print("No GSC properties found for this account.")
        return

    col_url = max(len(s.get("siteUrl", "")) for s in sites)
    col_url = max(col_url, 4)  # min width for "URL" header
    col_perm = 15

    sep = f"+{'-' * (col_url + 2)}+{'-' * (col_perm + 2)}+"
    header = f"| {'URL':<{col_url}} | {'Permission':<{col_perm}} |"

    print(f"\n{'='*60}")
    print(f"  Google Search Console Properties  ({len(sites)} found)")
    print(f"{'='*60}")
    print(sep)
    print(header)
    print(sep)

    for site in sites:
        url = site.get("siteUrl", "N/A")
        raw_perm = site.get("permissionLevel", "N/A")
        perm = PERMISSION_LABELS.get(raw_perm, raw_perm)
        print(f"| {url:<{col_url}} | {perm:<{col_perm}} |")

    print(sep)
    print(f"\n  Total: {len(sites)} propert{'y' if len(sites) == 1 else 'ies'}\n")


def main():
    parser = argparse.ArgumentParser(
        description="List Google Search Console properties via API"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--auth", action="store_true", help="Re-authenticate (clear saved token)"
    )
    parser.add_argument("--setup", action="store_true", help="Show setup instructions")
    args = parser.parse_args()

    if args.setup:
        print(SETUP_GUIDE)
        return

    _require_google_libs()

    if args.auth and TOKEN_FILE.exists():
        TOKEN_FILE.unlink()
        print("Saved token removed. A fresh authentication flow will start.\n")

    sites = fetch_properties()

    if args.json:
        print(json.dumps(sites, indent=2, ensure_ascii=False))
    else:
        print_table(sites)


if __name__ == "__main__":
    main()
