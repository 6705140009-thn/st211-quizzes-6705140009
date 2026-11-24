# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock
def test_mock_return_configured_value():
    mock = Mock()
    mock.get_data.return_value = "fake data"
    assert mock.get_data() == "fake data"

def test_mock_accept_any_call():
    mock = Mock()
    mock.anything()
    mock.whatever(1,2,3)

def test_mock_attribute_access():
    mock = Mock()
    mock.name = "TestUser"
    assert mock.name == "TestUser"
