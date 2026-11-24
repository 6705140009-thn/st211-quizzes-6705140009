# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from bank import BankAccount


@pytest.mark.parametrize("amount", [0, -1, -50])
def test_invalid_withdrawal_leaves_balance_unchanged(amount):
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Withdrawal must be positive"):
        account.withdraw(amount)
    assert account.balance == 100


def test_overdraft_leaves_balance_unchanged():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(101)
    assert account.balance == 100


def test_withdraw_entire_balance():
    account = BankAccount(100)
    assert account.withdraw(100) == 0


def test_negative_initial_balance_rejected():
    with pytest.raises(ValueError, match="Initial balance"):
        BankAccount(-1)


@pytest.mark.parametrize("amount", [0, -1])
def test_invalid_deposit_leaves_balance_unchanged(amount):
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Deposit must be positive"):
        account.deposit(amount)
    assert account.balance == 100
