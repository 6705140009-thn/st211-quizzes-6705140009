# Student: Thet Htoo Naing
# Student ID: 6705140009

def test_deposit(account):
    assert account.deposit(50) == 150


def test_withdraw(account):
    assert account.withdraw(30) == 70
