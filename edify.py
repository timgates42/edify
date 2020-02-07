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
    for retry in range(2):
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-U", "pip",
            ])
        except subprocess.CalledProcessError:
            if retry:
                raise
            subprocess.check_call([
                "sudo", "apt", "install", "curl",
            ])
            subprocess.check_call([
                "curl", "https://bootstrap.pypa.io/get-pip.py", "-o", "get-pip.py",
            ])
            subprocess.check_call([
                "sudo", sys.executable, "get-pip.py",
            ])
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-U", "pipenv",
    ])
    subprocess.check_call([
        sys.executable, "-m", "pipenv", "install",
        "--system", "--deploy",
    ])
    subprocess.check_call([
        sys.executable, "-m", "edification",
    ])

if __name__ == '__main__':
    main()
