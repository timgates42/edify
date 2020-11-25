"""
Simple general installations
"""

import subprocess


def gensetup(nosudo):
    """
    Simple general installations
    """
    if nosudo:
        return
    subprocess.check_call(
        ["sudo", "apt", "install", "-y", "links", "expect", "jq"]
    )
