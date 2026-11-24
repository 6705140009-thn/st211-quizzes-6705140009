# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount(100)
