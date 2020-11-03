"""
cleanup python
"""

import subprocess


def get_system_py():
    """
    Direct version of the system python version
    """
    release = subprocess.check_output(["lsb_release", "-s", "-r"])
    return {
        "18.04": "python3.6"
    }.get(release, "python3.8")

def pysetup():
    """
    runs python setup
    """
    check = subprocess.call(
        [get_system_py(), "-c", "__import__('isort');__import__('black')"]
    )
    if check == 0:
        return
    exit_py38()
    try:
        setup_regular_py()
    finally:
        enter_py38()


def enter_py38():
    """
    After installing standard python pip and package we resume py 3.8
    """
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.call(aptins + ["python3.8-distutils", "python3.8-lib2to3"])


def exit_py38():
    """
    To install standard python pip we need to temporarily remove these
    """
    aptremove = ["sudo", "apt-get", "remove", "-y"]
    subprocess.call(aptremove + ["python3.8-distutils", "python3.8-lib2to3"])


def setup_regular_py():
    """
    Install python 3.6 isort
    """
    pyexe = get_system_py()
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.call(aptins + ["python3-distutils"])
    subprocess.call(["sudo", pyexe, "get-pip.py"])
    subprocess.call(["sudo", pyexe, "-m", "pip", "install", "isort"])
    subprocess.call(["sudo", pyexe, "-m", "pip", "install", "black"])
