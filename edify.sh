#!/usr/bin/env bash

#################################################
# The main entry point to start the edification #
#################################################

set -euo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if ! which python3.8 >/dev/null 2>/dev/null ; then
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.8
fi
python3.8 "${BASEDIR}/edify.py"
