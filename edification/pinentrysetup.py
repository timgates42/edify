"""
Set curses as default pinentry
"""

import subprocess  # nosec # noqa


def pinentrysetup():
    """
    Set curses as default pinentry
    """
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
