#!/usr/bin/env bash

set -Eeuo pipefail

cd "$(dirname "$0")"

source venv/bin/activate

python3 main.py
