# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import patch
import pytest
from weather import describe_weather

def test_hot_weather():
    with patch("weather.get_temperature", return_value=30):
        assert describe_weather() == "Hot"

def test_freezing_weather():
    with patch("weather.get_temperature", return_value=-5):
        assert describe_weather() == "Freezing"


@pytest.mark.parametrize("temperature, expected", [
    (-1, "Freezing"), (0, "Cold"), (14, "Cold"),
    (15, "Pleasant"), (24, "Pleasant"), (25, "Hot"),
])
def test_weather_boundaries(temperature, expected):
    with patch("weather.get_temperature", return_value=temperature) as mock_temp:
        assert describe_weather() == expected
    mock_temp.assert_called_once_with()
