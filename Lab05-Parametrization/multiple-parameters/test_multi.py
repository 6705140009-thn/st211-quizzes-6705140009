# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest

@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    assert x + y > 0
    print(f"\n Testing x={x}, y={y}")
