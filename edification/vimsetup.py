
import pathlib
import shutil
import subprocess

from edification.storage import get_basedir

def vimsetup():
    src = get_basedir() / "data" / ".vimrc"
    trg = pathlib.Path.home() / ".vimrc"
    shutil.copy(src, trg)
    pathogen()

def pathogen():
    autoload = pathlib.Path.home() / ".vim" / "autoload"
    paths = [
        pathlib.Path.home() / ".vim",
        pathlib.Path.home() / ".vim" / "bundle",
    ]
    for path in paths:
        path.mkdir(exist_ok=True, parents=True)
    target = autoload / "pathogen.vim"
    subprocess.check_call([
        "curl", "-LSso", str(target), "https://tpo.pe/pathogen.vim"
    ])
