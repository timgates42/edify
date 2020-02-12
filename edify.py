# /usr/bin/env python
"""
Load essentials and run python entry point
"""

import subprocess
import sys


def main():
    """
    Load essentials and run python entry point
    """
    if sys.version_info[:2] != (3, 8):
        print("Run edify.sh to install edify", sys=sys.stderr)
        sys.exit(1)
    aptinst = ["sudo", "-H", "apt", "install", "-y"]
    packages = [
        "git",
        "unixodbc",
        "unixodbc-dev",
        "libldap2-dev",
        "libsasl2-dev",
        "python3.8-dev",
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
        except subprocess.CalledProcessError:
            if retry:
                raise
            subprocess.check_call(aptinst + "python3.8-distutils")
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
    subprocess.check_call([sys.executable, "-m", "edification"])


if __name__ == "__main__":
    main()
