#!/usr/bin/env bash
# Materializes the GCP service account JSON from an env var into a file on disk.
# Required because mcp-server-gsc needs a file path (GOOGLE_APPLICATION_CREDENTIALS),
# and the remote container is ephemeral — we can't commit the JSON.
#
# Set GCP_SERVICE_ACCOUNT_JSON in the remote environment with the full JSON content.

set -euo pipefail

TARGET="${GOOGLE_APPLICATION_CREDENTIALS:-/tmp/gcp-service-account.json}"

if [[ -z "${GCP_SERVICE_ACCOUNT_JSON:-}" ]]; then
  echo "[materialize-gcp-credentials] GCP_SERVICE_ACCOUNT_JSON not set — skipping. GSC MCP will fail to authenticate." >&2
  exit 0
fi

mkdir -p "$(dirname "$TARGET")"
printf '%s' "$GCP_SERVICE_ACCOUNT_JSON" > "$TARGET"
chmod 600 "$TARGET"
echo "[materialize-gcp-credentials] Wrote service account JSON to $TARGET" >&2
