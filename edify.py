# /usr/bin/env python
"""
Load essentials and run python entry point
"""

import os
import subprocess
import sys


def main():
    """
    Load essentials and run python entry point
    """
    try:
        pyver = os.environ["PYVER"]
    except KeyError:
        pyver = "1.0"
    pyvertup = tuple(int(val) for val in pyver.split("."))
    if sys.version_info[:2] != pyvertup:
        print("Run edify.sh to install edify", file=sys.stderr)
        sys.exit(1)
    aptinst = ["sudo", "-H", "apt", "install", "-y"]
    packages = [
        "git",
        "unixodbc",
        "unixodbc-dev",
        "libldap2-dev",
        "libsasl2-dev",
        f"python{pyver}-dev",
        "build-essential",
        "vim",
        "curl",
        "pass",
    ]
    subprocess.check_call(aptinst + packages)
    for retry in range(2):
        try:
            pipupgrade = [
                "sudo",
                "-H",
                sys.executable,
                "-m",
                "pip",
                "install",
                "-U",
                "pip",
            ]
            subprocess.check_call(pipupgrade)
            break
        except subprocess.CalledProcessError:
            if retry:
                raise
            subprocess.check_call(aptinst + [f"python{pyver}-distutils"])
            getpip = [
                "curl",
                "https://bootstrap.pypa.io/get-pip.py",
                "-o",
                "get-pip.py",
            ]
            subprocess.check_call(getpip)
            runpip = ["sudo", "-H", sys.executable, "get-pip.py"]
            subprocess.check_call(runpip)
    pipenvins = ["sudo", "-H", sys.executable, "-m", "pip", "install", "-U", "pipenv"]
    subprocess.check_call(pipenvins)
    for retry in range(2):
        try:
            subprocess.check_call(
                [
                    "sudo",
                    "-H",
                    sys.executable,
                    "-m",
                    "pipenv",
                    "install",
                    "--system",
                    "--deploy",
                ]
            )
            break
        except subprocess.CalledProcessError:
            if retry:
                raise
            sysinss = [
                "httplib2",
                "pyyaml",
                "simplejson",
                "psutil",
            ]
            pipenvins = [
                "sudo",
                "-H",
                sys.executable,
                "-m",
                "pip",
                "install",
                "--ignore-installed",
                "-U",
            ]
            for sysins in sysinss:
                subprocess.check_call(pipenvins + [sysins])
    subprocess.check_call([sys.executable, "-m", "edification"])


if __name__ == "__main__":
    main()
