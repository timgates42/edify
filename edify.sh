#!/usr/bin/env bash

#################################################
# The main entry point to start the edification #
#################################################

set -euo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PYVER="3.9"
export PYVER
PYTHON="python${PYVER}"
export PYTHON
if ! which "${PYTHON}" >/dev/null 2>/dev/null ; then
  sudo -H update-ca-certificates
  sudo -H add-apt-repository -y ppa:deadsnakes/ppa
  sudo -H apt-get -y update
  sudo -H apt-get -y install "${PYTHON}"
fi
"${PYTHON}" "${BASEDIR}/edify.py"
