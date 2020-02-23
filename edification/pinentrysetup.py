"""
Set curses as default pinentry
"""

import subprocess


def pinentrysetup():
    """
    Set curses as default pinentry
    """
    subprocess.call(
        ["sudo", "update-alternatives", "--set", "pinentry", "/usr/bin/pinentry-curses"]
    )
