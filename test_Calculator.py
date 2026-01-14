import pytest
from Calculator import multiply

def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6
    assert multiply(5, 4) == 20

def test_multiply_negative_numbers():
    assert multiply(-2, 3) == -6
    assert multiply(-5, -4) == 20

def test_multiply_with_zero():
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0

def test_multiply_floats():
    assert multiply(2.5, 4) == 10.0
    assert multiply(1.5, 2.5) == 3.75