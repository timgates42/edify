"""
Docker install
"""

import getpass
import os
import pathlib
import subprocess  # noqa # nosec
import sys

from plumbum import FG, local


def dockersetup():
    """
    Docker install
    """
    dockerinstall()
    dockernet()


def dockerinstall():
    """
    Command install
    """
    if subprocess.call(["which", "docker"]) == 0:  # noqa # nosec
        return
    sudo = local["sudo"]
    curl = local["curl"]
    _ = (
        curl["-fsSL", "https://download.docker.com/linux/ubuntu/gpg"]
        | sudo["apt-key", "add", "-"]
    ) & FG
    lsb_release = local["lsb_release"]
    lsb_info = lsb_release("-cs")
    _ = (
        sudo[
            "add-apt-repository",
            f"deb [arch=amd64]"
            f" https://download.docker.com/linux/ubuntu"
            f" {lsb_info} stable",
        ]
        & FG
    )
    _ = sudo["apt-get", "update"] & FG
    _ = sudo[
        "apt-get", "install", "-y", "docker-ce", "docker-ce-cli", "containerd.io"
    ] & FG
    _ = sudo["usermod", "-a", "-G", "docker", getpass.getuser()] & FG


def get_basedir():
    """
    Locate the root directory of this project
    """
    this_py_path = pathlib.Path(sys.modules[__name__].__file__)
    return this_py_path.absolute().parent.parent


def dockernet():
    """
    Setup docker network
    """
    daemonpath = "/etc/docker/daemon.json"
    if os.path.isfile(daemonpath):
        return
    cppath = get_basedir() / "daemon.json"
    sudo = local["sudo"]
    _ = sudo["cp", str(cppath), daemonpath] & FG
    _ = sudo["/etc/init.d/docker", "restart"] & FG
