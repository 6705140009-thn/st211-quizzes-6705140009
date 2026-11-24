# Student: Thet Htoo Naing
# Student ID: 6705140009

from access import check_access
def test_admin_active():
    assert check_access("admin", True) == "granted"

def test_user_inactive():
    assert check_access("user", False) == "denied"
