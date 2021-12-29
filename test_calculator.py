import pytest
import calculator as cal

# ADD
def test_add_two_numbers():
    assert cal.add(1,1) == 2

def test_add_two_strings_return_none():
    assert cal.add('a','b') is None

def test_add_integer_to_string_return_none():
    assert cal.add(1,'a') is None

# Subtract
def test_subtract_two_integers_return_integer():
    assert cal.subtract(2,1) == 1

def test_subtract_two_strings_return_none():
    assert cal.subtract('a','b') is None