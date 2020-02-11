"""
Docker install
"""

import getpass
import subprocess

from plumbum import FG, local


def dockersetup():
    """
    Docker install
    """
    if subprocess.call(["which", "docker"]):
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
    _ = sudo["apt-get", "install", "docker-ce", "docker-ce-cli", "containerd.io"] & FG
    _ = sudo["usermod", "-a", "-G", "docker", getpass.getuser()] & FG
