# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from bank import BankAccount


@pytest.fixture
def account_factory():
    def create(balance=0):
        return BankAccount(balance)
    return create


def test_factory_creates_independent_accounts(account_factory):
    first = account_factory(100)
    second = account_factory(50)
    first.withdraw(30)
    assert first.balance == 70
    assert second.balance == 50


def test_factory_default_balance(account_factory):
    assert account_factory().balance == 0
