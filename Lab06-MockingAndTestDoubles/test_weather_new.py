# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import patch
from weather_new import describe_weather


@patch("weather_new.get_temperature")
def test_pleasant_weather(mock_temp):
    mock_temp.return_value = 20
    assert describe_weather() == "Pleasant"


@patch("weather_new.get_temperature")
def test_cold_weather(mock_temp):
    mock_temp.return_value = 5
    assert describe_weather() == "Cold"
