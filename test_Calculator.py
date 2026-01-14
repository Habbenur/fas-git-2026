import pytest
from Calculator import multiply, add
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

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 4) == 9

def test_add_negative_numbers():
    assert add(-2, 3) == 1
    assert add(-5, -4) == -9

def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_floats():
    assert add(2.5, 4.5) == 7.0
    assert add(1.5, 2.5) == 4.0
    assert multiply(1.5, 2.5) == 3.75
