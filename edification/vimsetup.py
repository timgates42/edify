
import pathlib
import shutil
import subprocess

from edification.storage import get_basedir

def vimsetup():
    src = get_basedir() / "data" / ".vimrc"
    trg = pathlib.Path.home() / ".vimrc"
    shutil.copy(src, trg)
    pathogen()
    syntastic()

def pathogen():
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
    subprocess.check_call([
        "curl", "-LSso", str(target), "https://tpo.pe/pathogen.vim"
    ])

def syntastic():
    bundle = pathlib.Path.home() / ".vim" / "bundle"
    synpath = bundle / "syntastic"
    if synpath.is_dir():
        print("git update syntastic")
    else:
        subprocess.check_call([
            "git", "clone", "--depth=1",
            "https://github.com/vim-syntastic/syntastic.git",
        ], cwd=str(bundle))
