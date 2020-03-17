"""
Setup git global config
"""
import subprocess

from edification import storage


def gitsetup():
    """
    Setup git global config
    """
    globalconf = ["git", "config", "--global"]
    subprocess.check_call(
        globalconf + ["user.name", storage.get_user_name()]
    )
    subprocess.check_call(
        globalconf + ["user.email", storage.get_user_email()]
    )
    gpgsign = globalconf + ["commit.gpgsign", "true"]
    subprocess.check_call(gpgsign)
    signkey = globalconf + ["user.signingkey", storage.get_user_email()]
    subprocess.check_call(signkey)
    subprocess.check_call(
        globalconf + ["fetch.prune", "true"]
    )
