
import os
import pathlib
import subprocess

def pysetup():
    target = pathlib.Path("/usr/bin/python")
    if not target.exists():
        source = pathlib.Path("/usr/bin/python3.8")
        subprocess.check_call([
            "sudo", "ln", str(source), str(target)
        ])

