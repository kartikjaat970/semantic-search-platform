#!/usr/bin/env bash
# Starts db + backend + frontend in Docker, wired up for Codespaces URLs.
set -e
cd "$(dirname "$0")/.."

docker compose -f docker-compose.yml -f docker-compose.codespaces.yml up -d --build

# The browser calls the backend directly, so port 8000 must be public.
# Retry for a while because the port only exists once the backend is listening.
for i in $(seq 1 60); do
  if gh codespace ports visibility 8000:public -c "$CODESPACE_NAME" >/dev/null 2>&1; then
    echo "Port 8000 set to public."
    break
  fi
  sleep 5
done

echo "Ready: open the 'Frontend' port (3000) from the Ports tab."
