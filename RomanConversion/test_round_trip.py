# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from roman import integer_to_roman, roman_to_integer


@pytest.mark.parametrize("number", [1, 4, 9, 40, 90, 400, 900, 2026, 3999])
def test_round_trip(number):
    assert roman_to_integer(integer_to_roman(number)) == number


@pytest.mark.parametrize("number", [0, -1, 4000])
def test_out_of_range_integer_rejected(number):
    with pytest.raises(ValueError, match="1 to 3999"):
        integer_to_roman(number)


@pytest.mark.parametrize("number", [True, False, 1.5, "10", None])
def test_non_integer_rejected(number):
    with pytest.raises(TypeError):
        integer_to_roman(number)


@pytest.mark.parametrize("value", [None, 10, True])
def test_non_string_roman_rejected(value):
    with pytest.raises(TypeError):
        roman_to_integer(value)
