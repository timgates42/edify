"""
Load and run all machine setup
"""

import sys

import edification.bashsetup
import edification.dockersetup
import edification.gensetup
import edification.gitsetup
import edification.gpgsetup
import edification.meticuloussetup
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
    nosudo = "--no-sudo" in sys.argv
    edification.storage.prepare()
    edification.gpgsetup.gpgsetup()
    edification.meticuloussetup.meticuloussetup(nosudo)
    edification.gensetup.gensetup(nosudo)
    edification.vimsetup.vimsetup()
    edification.gitsetup.gitsetup()
    edification.pinentrysetup.pinentrysetup(nosudo)
    edification.pysetup.pysetup(nosudo)
    edification.bashsetup.bashsetup()
    edification.dockersetup.dockersetup(nosudo)
    edification.terraformsetup.terraformsetup()
    edification.tmuxsetup.tmuxsetup()


if __name__ == "__main__":
    main()
