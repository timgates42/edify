"""
Install terraform
"""
import pathlib

from plumbum import FG, local

from edification.storage import get_basedir


def terraformsetup():
    """
    Install terraform
    """
    target = pathlib.Path("/") / "usr" / "bin" / "terraform"
    if target.exists():
        return
    curl = local["curl"]
    unzip = local["unzip"]
    sudo = local["sudo"]
    ziptarget = get_basedir() / "terraform_0.12.20_linux_amd64.zip"
    _ = (
        curl[
            "--output", ziptarget,
            "https://releases.hashicorp.com/terraform"
            "/0.12.20/terraform_0.12.20_linux_amd64.zip"
        ]
        & FG
    )
    with local.cwd(str(get_basedir())):
        _ = unzip["terraform_0.12.20_linux_amd64.zip"] & FG
    ziptarget.unlink()
    src = get_basedir() / "terraform"
    _ = sudo["mv", str(src), str(target)] & FG
