"""
Set curses as default pinentry
"""

import subprocess  # nosec # noqa


def pinentrysetup(nosudo):
    """
    Set curses as default pinentry
    """
    if nosudo:
        return
    subprocess.run(  # nosec # noqa
        [
            "sudo",
            "update-alternatives",
            "--set",
            "pinentry",
            "/usr/bin/pinentry-curses",
        ],
        check=True,
    )
