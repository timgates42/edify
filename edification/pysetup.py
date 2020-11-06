"""
cleanup python
"""

import os
import subprocess  # noqa # nosec


def get_system_py():
    """
    Direct version of the system python version
    """
    release = subprocess.check_output(["lsb_release", "-s", "-r"])  # noqa # nosec
    return {"18.04": "python3.6"}.get(release, "python3.8")


def pysetup():
    """
    runs python setup
    """
    check = subprocess.call(  # noqa # nosec
        [get_system_py(), "-c", "__import__('isort');__import__('black')"]
    )
    if check == 0:
        return
    pylatest = os.environ["PYVER"]
    exit_pylatest(pylatest)
    try:
        setup_regular_py()
    finally:
        enter_pylatest(pylatest)


def enter_pylatest(pylatest):
    """
    After installing standard python pip and package we resume py latest
    """
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.call(  # noqa # nosec
        aptins + [f"python{pylatest}-distutils", f"python{pylatest}-lib2to3"]
    )


def exit_pylatest(pylatest):
    """
    To install standard python pip we need to temporarily remove these
    """
    aptremove = ["sudo", "apt-get", "remove", "-y"]
    subprocess.call(  # noqa # nosec
        aptremove + [f"python{pylatest}-distutils", f"python{pylatest}-lib2to3"]
    )


def setup_regular_py():
    """
    Install python 3.6 isort
    """
    pyexe = get_system_py()
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.call(aptins + ["python3-distutils"])  # noqa # nosec
    subprocess.call(["sudo", pyexe, "get-pip.py"])  # noqa # nosec
    subprocess.call(["sudo", pyexe, "-m", "pip", "install", "isort"])  # noqa # nosec
    subprocess.call(["sudo", pyexe, "-m", "pip", "install", "black"])  # noqa # nosec
