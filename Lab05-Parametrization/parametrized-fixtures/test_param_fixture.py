# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest

@pytest.fixture(params=["sqlite", "postgres", "mysql"])
def database_type(request):
    # 'request' is a special built-in pytest fixture
    # request.param holds the current parameter value
    return request.param

def test_database_connection(database_type):
    print(f"\n Testing with {database_type}")
    assert database_type in ["sqlite", "postgres", "mysql"]
