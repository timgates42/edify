"""
tmux install
"""

import pathlib
import shutil
import subprocess

from plumbum import FG, local

from edification.storage import get_basedir


def tmuxsetup():
    """
    tmux install
    """
    source = get_basedir() / "data" / ".tmux.conf"
    target = pathlib.Path.home() / ".tmux.conf"
    shutil.copy(source, target)
    if subprocess.call(["which", "tmux"]) == 0:
        return
    sudo = local["sudo"]
    _ = sudo["apt-get", "install", "tmux"] & FG
