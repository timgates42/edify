"""
Install vim plugins
"""

import pathlib
import shutil
import subprocess

from edification.storage import get_basedir


def vimsetup():
    """
    Install vim plugins
    """
    src = get_basedir() / "data" / ".vimrc"
    trg = pathlib.Path.home() / ".vimrc"
    shutil.copy(src, trg)
    src = get_basedir() / "data" / ".isort.cfg"
    trg = pathlib.Path.home() / ".isort.cfg"
    shutil.copy(src, trg)
    pathogen_vundle()
    syntastic()


def pathogen_vundle():
    """
    Use pathogen and vundle package managers
    """
    autoload = pathlib.Path.home() / ".vim" / "autoload"
    bundle = pathlib.Path.home() / ".vim" / "bundle"
    paths = [
        pathlib.Path.home() / ".vim",
        bundle,
        autoload,
    ]
    for path in paths:
        path.mkdir(exist_ok=True, parents=True)
    target = autoload / "pathogen.vim"
    getpathogen = ["curl", "-LSso", str(target), "https://tpo.pe/pathogen.vim"]
    subprocess.check_call(getpathogen)
    target = bundle / "Vundle.vim"
    if not target.is_dir():
        getvundle = [
            "git",
            "clone",
            "https://github.com/VundleVim/Vundle.vim.git",
            target,
        ]
        subprocess.check_call(getvundle)
    else:
        print("git update vundle")


def syntastic():
    """
    Install syntastic
    """
    bundle = pathlib.Path.home() / ".vim" / "bundle"
    synpath = bundle / "syntastic"
    if synpath.is_dir():
        print("git update syntastic")
    else:
        subprocess.check_call(
            [
                "git",
                "clone",
                "--depth=1",
                "https://github.com/vim-syntastic/syntastic.git",
            ],
            cwd=str(bundle),
        )
