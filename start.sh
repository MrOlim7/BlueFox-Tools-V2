#!/usr/bin/env bash
# BlueFox v2.5 beta — Linux / macOS launcher
# ─────────────────────────────────────────────────────────────────────────────

set -e

PYTHON_BIN=""

# Find a compatible Python 3.10+ interpreter
for candidate in python3.12 python3.11 python3.10 python3 python; do
    if command -v "$candidate" &>/dev/null; then
        ver=$("$candidate" -c "import sys; print(sys.version_info >= (3,10))" 2>/dev/null)
        if [ "$ver" = "True" ]; then
            PYTHON_BIN="$candidate"
            break
        fi
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo ""
    echo "  [!] BlueFox requires Python 3.10 or higher."
    echo "      Install it from https://www.python.org/downloads/"
    echo ""
    exit 1
fi

echo ""
echo "  [>] Using $($PYTHON_BIN --version)"

# Check for a virtual environment
if [ -d ".venv" ]; then
    echo "  [>] Activating .venv ..."
    # shellcheck disable=SC1091
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "  [>] Activating venv ..."
    # shellcheck disable=SC1091
    source venv/bin/activate
fi

# Check dependencies
if ! "$PYTHON_BIN" -c "import requests" &>/dev/null 2>&1; then
    echo ""
    echo "  [!] Some dependencies are missing. Installing now ..."
    echo ""
    "$PYTHON_BIN" -m pip install -r requirements.txt --quiet
fi

echo "  [>] Launching BlueFox ..."
echo ""

"$PYTHON_BIN" BlueFox.py
