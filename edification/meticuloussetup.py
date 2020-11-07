"""
Setup for the meticulous project
"""

import subprocess  # noqa # nosec
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


def meticuloussetup():
    """
    Setup for the meticulous project
    """
    subprocess.call(["sudo", "apt-get", "install", "-y", "postgresql"])  # noqa # nosec
    subprocess.call(["sudo", "apt-get", "install", "-y", "apache2"])  # noqa # nosec
    sql = CREATE_USER % {"user": getuser()}
    subprocess.call(["sudo", "-u", "postgres", "psql", "-c", sql])  # noqa # nosec
    for dbname in (getuser(), "meticulous"):
        sql = CREATE_DB % {"db": dbname}
        subprocess.run(["sudo", "-u", "postgres", "psql"], input=sql, check=True)  # noqa # nosec
