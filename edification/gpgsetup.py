"""
Adjust password cache length
"""

import pathlib


def gpgsetup():
    """
    Adjust password cache length
    """
    basedir = pathlib.Path.home() / ".gnupg"
    agentconf = basedir / "gpg-agent.conf"
    if not basedir.is_dir():
        basedir.mkdir()
    if not agentconf.is_file():
        with open(agentconf, "w") as fobj:
            print(
                """
default-cache-ttl 34560000
max-cache-ttl 34560000
""",
                file=fobj,
            )
