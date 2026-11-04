#!/bin/sh
set -eu
CDPATH= cd "$(dirname "$0")"
if [ -n "${PYTHON:-}" ]; then
    if ! command -v "$PYTHON" >/dev/null 2>&1; then
        echo "SETUP FAILED: PYTHON points to an unavailable interpreter: $PYTHON" >&2
        echo "Set PYTHON to a Python 3.9+ executable path, then retry." >&2
        exit 2
    fi
    exec "$PYTHON" setup.py "$@"
fi

for PYTHON_BIN in python3 python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 python; do
    if command -v "$PYTHON_BIN" >/dev/null 2>&1 &&
       "$PYTHON_BIN" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)' 2>/dev/null; then
        exec "$PYTHON_BIN" setup.py "$@"
    fi
done
echo "SETUP FAILED: Python 3.9 or newer was not found." >&2
echo "Install Python from https://www.python.org/downloads/ and reopen your terminal." >&2
echo "If already installed elsewhere, run: PYTHON=/path/to/python3 ./setup.sh" >&2
exit 2
