"""
Setup python symlink
"""

import pathlib
import subprocess


def pysetup():
    """
    Setup python symlink
    """
    target = pathlib.Path("/usr/bin/python")
    if not target.exists():
        source = pathlib.Path("/usr/bin/python3.8")
        subprocess.check_call([
            "sudo", "ln", str(source), str(target)
        ])
