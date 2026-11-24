# Student: Thet Htoo Naing
# Student ID: 6705140009

import json
from pathlib import Path
import pytest

def load_cases():
    with Path(__file__).with_name("test_cases.json").open(encoding="utf-8") as f:
        data = json.load(f) # read the whole file
    return [(case["input"], case["expected"]) for case in data]

@pytest.mark.parametrize("text,expected", load_cases()) # loader runs at collection
def test_uppercase(text, expected):
    assert text.upper() == expected
