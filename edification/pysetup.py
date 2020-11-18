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
    pyinssetup()
    pypipsetup()


def pyinssetup():
    """
    Basic python install
    """
    check = subprocess.call(  # noqa # nosec
        [
            get_system_py(),
            "-c",
            "__import__('isort');__import__('black');__import__('yamllint');",
        ]
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
    subprocess.run(  # noqa # nosec
        aptins + [f"python{pylatest}-distutils", f"python{pylatest}-lib2to3"],
        check=True,
    )


def exit_pylatest(pylatest):
    """
    To install standard python pip we need to temporarily remove these
    """
    aptremove = ["sudo", "apt-get", "remove", "-y"]
    subprocess.run(  # noqa # nosec
        aptremove + [f"python{pylatest}-distutils", f"python{pylatest}-lib2to3"],
        check=True,
    )


def setup_regular_py():
    """
    Install python 3.6 isort
    """
    pyexe = get_system_py()
    aptins = ["sudo", "apt-get", "install", "-y"]
    subprocess.run(
        aptins + ["python3-venv", "python3-distutils"], check=True
    )  # noqa # nosec
    subprocess.run(["sudo", pyexe, "get-pip.py"], check=True)  # noqa # nosec
    subprocess.run(  # noqa # nosec
        ["sudo", pyexe, "-m", "pip", "install", "isort"], check=True
    )
    subprocess.run(  # noqa # nosec
        ["sudo", pyexe, "-m", "pip", "install", "black"], check=True
    )
    subprocess.run(  # noqa # nosec
        ["sudo", pyexe, "-m", "pip", "install", "yamllint"], check=True
    )


def pypipsetup():
    """
    Ensure artifactory available in pypi config
    """
