"""
IRESS custom certs
"""

import pathlib
import subprocess  # nosec # noqa
import sys


def prepare():
    """
    Run iress machine setup
    """
    prepare_certs()


def prepare_certs():
    """
    Copy over iress crt if not present and update root ca
    """
    iresscert = get_basedir() / "data" / "iress.crt"
    target = pathlib.Path("/usr/local/share/ca-certificate/iress.crt")
    if target.is_file():
        return
    subprocess.call(["sudo", "cp", str(iresscert), str(target)])  # nosec # noqa
    subprocess.call(["sudo", "update-ca-certificates"])  # nosec # noqa


def get_basedir():
    """
    Locate the root directory of this project
    """
    this_py_path = pathlib.Path(sys.modules[__name__].__file__)
    return this_py_path.absolute().parent.parent


if __name__ == "__main__":
    prepare()
