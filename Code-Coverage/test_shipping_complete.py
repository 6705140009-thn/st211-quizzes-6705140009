# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from shipping import calculate_shipping, free_shipping_eligible

def test_basic_shipping():
    assert calculate_shipping(10) == 20

def test_express_shipping():
    assert calculate_shipping(10, express=True) == 30

def test_negative_weight_raises():
    with pytest.raises(ValueError):
        calculate_shipping(-5)

def test_heavy_surcharge():
    assert calculate_shipping(150) == 350  # 150*2 + 50

def test_free_shipping_eligible():
    assert free_shipping_eligible(1000) is True
    assert free_shipping_eligible(1500) is True


def test_zero_weight_raises():
    with pytest.raises(ValueError, match="Weight must be positive"):
        calculate_shipping(0)


def test_surcharge_boundary():
    assert calculate_shipping(100) == 200
    assert calculate_shipping(101) == 252


def test_express_heavy_shipping():
    assert calculate_shipping(150, express=True) == 500


def test_below_free_shipping_threshold():
    assert free_shipping_eligible(999) is False
