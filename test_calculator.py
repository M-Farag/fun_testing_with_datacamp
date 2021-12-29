import pytest
import calculator as cal

def test_add_two_numbers():
    assert cal.add(1,1) == 2

def test_add_two_strings_return_none():
    assert cal.add('a','b') is None

def test_add_integer_to_string_return_none():
    assert cal.add(1,'a') is None