#!/bin/bash
set -eEuo pipefail
# the canonical path of this script
SELF_PATH=$(realpath -- "$0")
readonly SELF_PATH SELF_DIR=${SELF_PATH%/*}

logAndRun() {
  local hint='Run cmd: '
  if [ -t 1 ]; then
    printf '\e[1;30;46m%s%s\e[0m\n' "$hint" "$*"
  else
    echo '============================================================'
    echo "$hint$*"
    echo '============================================================'
  fi
  time "$@"
}

cd "$SELF_DIR"/..

logAndRun poetry run pytest --cov=src --cov-branch --cov-report=xml --color=auto
logAndRun poetry run flake8 src tests --color=auto
logAndRun poetry run isort src tests --check --diff --color
logAndRun poetry run mypy src --color-output
