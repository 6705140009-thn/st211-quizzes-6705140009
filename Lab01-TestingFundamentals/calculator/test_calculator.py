# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from calculator import add, divide


@pytest.mark.parametrize("left,right,expected", [(2, 3, 5), (-2, 2, 0), (0, 0, 0)])
def test_add(left, right, expected):
    # Arrange: parameters supply the inputs and expected value.
    result = add(left, right)  # Act
    assert result == expected  # Assert


def test_divide():
    assert divide(7, 2) == pytest.approx(3.5)


def test_division_by_zero():
    with pytest.raises(ValueError, match="Denominator must not be zero"):
        divide(5, 0)
