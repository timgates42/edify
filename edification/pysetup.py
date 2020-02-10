"""
cleanup python
"""

import pathlib
import subprocess


def pysetup():
    """
    runs python setup
    """
    cleanup_py38_mess()

def cleanup_py38_mess():
    # We needed these to get here but now they get in the way of the system
    # python so drop them.
    subprocess.call([
        "sudo", "apt-get", "remove", "python3.8-distutils", "python3.8-lib2to3"
    ])
