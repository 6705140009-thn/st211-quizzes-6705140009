# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock
import pytest

def test_side_effect_exception():
    mock = Mock()
    mock.login.side_effect = RuntimeError(
        "Invalid credentials"
    )
    with pytest.raises(RuntimeError, match="Invalid credentials"):
        mock.login()
    mock.login.assert_called_once_with()
