# Student: Thet Htoo Naing
# Student ID: 6705140009

from weather import describe_weather

def test_weather_description():
    result = describe_weather()
    assert result in ["Freezing", "Cold", "Pleasant", "Hot"]
