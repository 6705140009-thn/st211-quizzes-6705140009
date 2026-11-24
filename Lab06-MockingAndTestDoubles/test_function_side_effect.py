# Student: Thet Htoo Naing
# Student ID: 6705140009

from unittest.mock import Mock


def test_function_side_effect_uses_arguments():
    dependency = Mock()
    dependency.calculate.side_effect = lambda value: value * 2
    assert dependency.calculate(5) == 10
    assert dependency.calculate(12) == 24
    assert dependency.calculate.call_count == 2


def test_return_value_stays_constant():
    dependency = Mock()
    dependency.fetch.return_value = "STATIC"
    assert [dependency.fetch() for _ in range(3)] == ["STATIC"] * 3
