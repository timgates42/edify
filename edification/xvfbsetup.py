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
    prepare_xvfb()


def prepare_xvfb():
    """
    Copy over iress crt if not present and update root ca
    """
    service = get_basedir() / "data" / "xvfb.service"
    target = pathlib.Path("/") / "lib" / "systemd" / "system" / "xvfb.service"
    if target.is_file():
        return
    subprocess.call(["sudo", "apt", "install", "xvfb"])  # nosec # noqa
    subprocess.call(["sudo", "cp", str(service), str(target)])  # nosec # noqa
    subprocess.call(["sudo", "systemctl", "daemon-reload"])  # nosec # noqa
    subprocess.call(["sudo", "systemctl", "enable", "xvfb"])  # nosec # noqa
    subprocess.call(["sudo", "systemctl", "start", "xvfb"])  # nosec # noqa


def get_basedir():
    """
    Locate the root directory of this project
    """
    this_py_path = pathlib.Path(sys.modules[__name__].__file__)
    return this_py_path.absolute().parent.parent


if __name__ == "__main__":
    prepare()
