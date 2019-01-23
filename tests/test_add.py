"""
Tests the add() fuction of the calculator.abs
"""
import pytest

from calculator import add

def test_two_plus_two():
    """
    if given  and 2 as parameters, 4 should be returned.
    """
    assert add(2, 2) == 4

def test_three_and_three():
    """
    If given 3 and 3, 6 should be returned.
    """
    assert add(3, 3) == 6

def test_no_parameters():
    """
    If no parameters, 0 should be returned.
    """
    assert add() == 0

def test_one_two_three():
    """
    Given the values 1, 2 and 3 as parameters, 6 should be returned.
    """
    assert add(1, 2, 3) == 6

def test_negative_values():
    """
    Assert the negative value works
    """
    assert add(-1, -1, -1, -1, -1) == -5

def test_decimal_values():
    """
    Asser that 0.1, 0.1 and 0.1 equals 0.3
    """
    #assert round(add(0.1, 0.1, 0.1), 2) == round(0.3, 2)
    assert add(0.1, 0.1, 0.1) == pytest.approx(0.3)
