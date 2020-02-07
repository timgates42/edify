
from edification import storage
import subprocess

def gitsetup():
    subprocess.check_call([
        "git", "config", "--global", "user.name",
        storage.get_user_name(),
    ])
    subprocess.check_call([
        "git", "config", "--global", "user.email",
        storage.get_user_email(),
    ])
