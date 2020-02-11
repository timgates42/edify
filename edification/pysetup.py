"""
cleanup python
"""

import subprocess


def pysetup():
    """
    runs python setup
    """
    check = subprocess.call(
        ["python3.6", "-c", "__import__('isort');__import__('black')"]
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
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.call(aptins + ["python3-distutils"])
    subprocess.call(["sudo", "python3.6", "get-pip.py"])
    subprocess.call(["sudo", "python3.6", "-m", "pip", "install", "isort"])
    subprocess.call(["sudo", "python3.6", "-m", "pip", "install", "black"])
