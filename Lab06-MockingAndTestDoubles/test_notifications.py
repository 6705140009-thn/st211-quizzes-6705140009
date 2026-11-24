# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import patch
from notifications import notify_user


def test_notify_user_without_sending_email():
    with patch("notifications.send_email") as mock_send:
        mock_send.return_value = True

        result = notify_user("student@siam.ac.th")

    assert result == "Notified student@siam.ac.th"
    mock_send.assert_called_once_with("student@siam.ac.th", "Welcome!")
