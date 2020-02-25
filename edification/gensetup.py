"""
Simple general installations
"""

import subprocess


def gensetup():
    """
    Simple general installations
    """
    subprocess.check_call([
        'sudo', 'apt', 'install', '-y', 'links'
    ])
