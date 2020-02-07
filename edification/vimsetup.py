
import pathlib
import shutil

from edification.storage import get_basedir

def vimsetup():
    src = get_basedir() / "data" / ".vimrc"
    trg = pathlib.Path.home() / ".vimrc"
    shutil.copy(src, trg)
