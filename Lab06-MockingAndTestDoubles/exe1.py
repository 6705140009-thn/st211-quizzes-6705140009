# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock
def test_mock_basics():
    mock = Mock()
    result = mock.whatever(1, 2, 3)
    print(result)
    assert isinstance(result, Mock)
