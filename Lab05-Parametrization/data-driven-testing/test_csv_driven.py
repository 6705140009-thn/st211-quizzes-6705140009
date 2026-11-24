# Student: Thet Htoo Naing
# Student ID: 6705140009

import csv
from pathlib import Path

import pytest
from validate import is_valid_login

def load_login_cases():
    cases = []
    with Path(__file__).with_name("logins.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f): # reads header row as dict keys
            if row["valid"] not in {"True", "False"}:
                raise ValueError(f"Invalid boolean in login data: {row['valid']}")
            expected = row["valid"] == "True"
            cases.append((row["username"], row["password"], expected))
    return cases

@pytest.mark.parametrize("username,password,expected", load_login_cases())
def test_login_validation(username, password, expected):
    assert is_valid_login(username, password) == expected
