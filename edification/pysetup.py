"""
cleanup python
"""

import os
import pathlib
import shutil
import subprocess  # noqa # nosec
import sys


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
    subprocess.run(  # noqa # nosec
        aptins + ["python3-venv", "python3-distutils"], check=True
    )
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


def get_basedir():
    """
    Locate the root directory of this project
    """
    this_py_path = pathlib.Path(sys.modules[__name__].__file__)
    return this_py_path.absolute().parent.parent


def pypipsetup():
    """
    Ensure artifactory available in pypi config
    """
    pypirc = get_basedir() / "data" / ".pypirc"
    pipconf = get_basedir() / "data" / "pip.conf"
    pipdir = pathlib.Path.home() / ".pip"
    if not pipdir.is_dir():
        pipdir.mkdir()
    target = pipdir / "pip.conf"
    if not target.is_file():
        shutil.copy(pipconf, target)
    target = pathlib.Path.home() / ".pypirc"
    if not target.is_file():
        shutil.copy(pypirc, target)
    subprocess.run(["sudo", "mkdir", "-p", "/root/.pip"], check=True)  # noqa # nosec
    subprocess.run(  # noqa # nosec
        ["cp", str(pipconf), "/root/.pip/pip.conf"], check=True
    )
    subprocess.run(  # noqa # nosec
        ["cp", str(pypirc), "/root/.pypirc"], check=True
    )
