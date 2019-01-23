"""
Tests the add() fuction of the calculator.abs
"""
from calculator import add

def test_two_plus_two():
    """
    if given  and 2 as parameters, 4 should be returned.abs
    """
    assert add(2, 2) == 4
