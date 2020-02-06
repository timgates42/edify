#/usr/bin/env python

import sys
import subprocess

def main():
    if sys.version_info[:2] != (3, 8):
        print("Run edify.sh to install edify", sys=sys.stderr)
        sys.exit(1)
    subprocess.check_call([
        "sudo", "apt", "install", "python3.8-dev",
    ])
    subprocess.check_call([
        "sudo", "apt", "install", "python3.8-distutils",
    ])
    subprocess.check_call([
        sys.executable, "-m", "pipenv", "install",
        "--system", "--deploy",
    ])
    print("""
    echo run the system based python to install the following...
    echo 
    echo install pip
    echo install pipenv
    echo install Pipefile requirements
    echo run edify.py
    echo install .vimrc
    """)

if __name__ == '__main__':
    main()
