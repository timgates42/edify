"""
Setup for the meticulous project
"""

import pathlib
import subprocess  # noqa # nosec
import sys
from getpass import getuser

CREATE_USER = """\
DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = '%(user)s') THEN

      CREATE ROLE %(user)s;
   END IF;
END
$do$;
"""

CREATE_DB = """
SELECT 'CREATE DATABASE %(db)s'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '%(db)s')\\gexec
"""

GRANT = """
GRANT ALL PRIVILEGES ON DATABASE %(db)s TO %(user)s;
"""


def meticuloussetup():
    """
    Setup for the meticulous project
    """
    rproxy()
    meticulousdb()


def get_basedir():
    """
    project root path
    """
    return pathlib.Path(sys.modules[__name__].__file__).resolve().parent.parent


def rproxy():
    """
    Setup the reverse proxy
    """
    subprocess.run(  # noqa # nosec
        ["sudo", "apt-get", "install", "-y", "apache2"], check=True
    )
    target = pathlib.Path("/etc/apache2/conf-available/meticulous.conf")
    src = get_basedir() / "apache" / "meticulous.conf"
    if not target.is_file():
        subprocess.run(  # noqa # nosec
            ["sudo", "cp", str(src), str(target)], check=True
        )


def meticulousdb():
    """
    Setup db access
    """
    subprocess.run(  # noqa # nosec
        ["sudo", "apt-get", "install", "-y", "postgresql"], check=True
    )
    sql = CREATE_USER % {"user": getuser()}
    subprocess.run(  # noqa # nosec
        ["sudo", "-u", "postgres", "psql", "-c", sql], check=True
    )
    for dbname in (getuser(), "meticulous"):
        sql = (CREATE_DB % {"db": dbname}).encode("ascii")
        subprocess.run(  # noqa # nosec
            ["sudo", "-u", "postgres", "psql"], input=sql, check=True
        )
        sql = GRANT % {"user": getuser(), "db": dbname}
        subprocess.run(  # noqa # nosec
            ["sudo", "-u", "postgres", "psql", "-c", sql], check=True
        )
