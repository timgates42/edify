"""
Load edify bash in home .bashrc
"""

import io
import pathlib
import re

from edification.storage import get_basedir


def bashsetup():
    """
    check .bashrc sources the edify
    """
    if check_present():
        return
    target = get_basedir() / "data" / "bashrc.sh"
    fpath = pathlib.Path.home() / ".bashrc"
    with io.open(fpath, "a", encoding="utf-8") as fobj:
        print("", file=fobj)
        print(f"source {target}", file=fobj)


def check_present():
    """
    Look for the source edify line
    """
    fpath = pathlib.Path.home() / ".bashrc"
    with io.open(fpath, "r", encoding="utf-8") as fobj:
        for line in fobj:
            if re.search("^source.*edify", line):
                return True
    return False
