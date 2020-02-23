"""
Load and run all machine setup
"""

import edification.bashsetup
import edification.dockersetup
import edification.gitsetup
import edification.pinentrysetup
import edification.pysetup
import edification.storage
import edification.terraformsetup
import edification.tmuxsetup
import edification.vimsetup


def main():
    """
    Run all machine setup
    """
    edification.storage.prepare()
    edification.vimsetup.vimsetup()
    edification.gitsetup.gitsetup()
    edification.pinentrysetup.pinentrysetup()
    edification.pysetup.pysetup()
    edification.bashsetup.bashsetup()
    edification.dockersetup.dockersetup()
    edification.terraformsetup.terraformsetup()
    edification.tmuxsetup.tmuxsetup()


if __name__ == "__main__":
    main()
