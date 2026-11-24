# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from mathutils import factorial

@pytest.mark.parametrize("number, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial(number, expected):
    assert factorial(number) == expected


def test_negative_factorial_rejected():
    with pytest.raises(ValueError, match="Negative not allowed"):
        factorial(-1)
