"""
Record current progress to avoid reprocessing
"""

import json
import pathlib
import sqlite3
import sys

from PyInquirer import prompt


def get_input(message):
    """
    Call PyInquirer/prompt-toolkit to make a simple input
    """
    menu = [{"type": "input", "name": "option", "message": message}]
    answers = prompt(menu)
    option = answers.get("option")
    return option


def prepare():
    """
    Ensure current db is ready for use
    """
    con = get_db()
    if not check_table_exists(con, "config"):
        sql = "CREATE TABLE config ( key text, value text )"
        con.execute(sql)


def get_value(key, deflt=None):
    """
    Retrieve a stored key value or return a default
    """
    con = get_db()
    sql = "SELECT value FROM config WHERE key = ?"
    for (value,) in con.execute(sql, (key,)):
        return value
    return deflt


def set_value(key, value):
    """
    Remove any old key values and insert a new key/value
    """
    con = get_db()
    sql = "DELETE FROM config WHERE key = ?"
    con.execute(sql, (key,))
    sql = "INSERT INTO config ( key, value ) VALUES (?, ?)"
    con.execute(sql, (key, value))
    con.commit()


def get_json_value(key, deflt=None):
    """
    Load a Json value for the specified key
    """
    deflt = json.dumps(deflt)
    jsonval = get_value(key, deflt=deflt)
    return json.loads(jsonval)


def set_json_value(key, value):
    """
    Serialize and save a Json value
    """
    set_value(key, json.dumps(value))


def check_table_exists(con, table_name):
    """
    Look in the database to see if table exists
    """
    sql = "SELECT name FROM sqlite_master WHERE" " type='table' AND name=?"
    for _ in con.execute(sql, (table_name,)):
        return True
    return False


def get_db():
    """
    Connect to the database
    """
    dbpath = get_basedir() / "sqlite.db"
    return sqlite3.connect(str(dbpath))


def get_basedir():
    """
    Locate the root directory of this project
    """
    this_py_path = pathlib.Path(sys.modules[__name__].__file__)
    return this_py_path.absolute().parent.parent


def get_user_name():
    """
    Get or request user name
    """
    return get_cached_input_value("user_name")


def get_cached_input_value(key):
    """
    Get or request a value
    """
    value = get_json_value(key)
    if value:
        return value
    value = get_input(f"{key}: ")
    set_json_value(key, value)
    return value


def get_user_email():
    """
    Get or request user email
    """
    return get_cached_input_value("user_email")


if __name__ == "__main__":
    prepare()
