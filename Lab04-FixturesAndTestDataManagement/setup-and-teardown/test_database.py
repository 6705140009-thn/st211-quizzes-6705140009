# Student: Thet Htoo Naing
# Student ID: 6705140009

import sqlite3
import pytest


@pytest.fixture
def database():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE students (id TEXT, name TEXT)")
    try:
        yield connection
    finally:
        connection.close()


def test_insert_student(database):
    database.execute("INSERT INTO students VALUES (?, ?)",
                     ("6705140009", "Thet Htoo Naing"))
    assert database.execute("SELECT name FROM students WHERE id = ?",
                            ("6705140009",)).fetchone() == ("Thet Htoo Naing",)


def test_new_database_is_empty(database):
    assert database.execute("SELECT COUNT(*) FROM students").fetchone()[0] == 0
