# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock


def test_was_called():
    mock = Mock()
    mock.save()
    mock.save.assert_called()


def test_was_called_once():
    mock = Mock()
    mock.save()
    mock.save.assert_called_once()
