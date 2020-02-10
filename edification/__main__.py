"""
Load and run all machine setup
"""

import edification.bashsetup
import edification.gitsetup
import edification.pysetup
import edification.storage
import edification.vimsetup


def main():
    """
    Run all machine setup
    """
    edification.storage.prepare()
    edification.vimsetup.vimsetup()
    edification.gitsetup.gitsetup()
    edification.pysetup.pysetup()
    edification.bashsetup.bashsetup()


if __name__ == "__main__":
    main()
