# Student: Thet Htoo Naing
# Student ID: 6705140009

from access import check_access
def test_admin_active():
    assert check_access("admin", True) == "granted"

def test_admin_inactive():
    assert check_access("admin", False) == "denied"

def test_non_admin_active():
    assert check_access("user", True) == "denied"

def test_non_admin_inactive():
    assert check_access("user", False) == "denied"
