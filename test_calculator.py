import pytest
import calculator as cal

# ADD
def test_add_two_numbers():
    assert cal.add(1,1) == 2

def test_add_two_strings_return_exception_type_error():
    with pytest.raises(TypeError) as exception_info:
        cal.add('a','b')

def test_add_integer_to_string_return_none():
    with pytest.raises(TypeError) as exception_info:
        cal.add(1,'a')
    assert exception_info.match('You cannot add strings')

# Subtract
def test_subtract_two_integers_return_integer():
    results = cal.subtract(2,1)
    assert isinstance(results,int),"{} is not an integer".format(results)
    assert  results == 1

def test_subtract_two_strings_return_none():
    assert cal.subtract('a','b') is None

def test_subtract_integer_and_string_return_none():
    assert cal.subtract(1,'n') is None

def test_subtract_two_integers_can_return_negative_value():
    assert cal.subtract(2,3) == -1

def test_subtract_float_and_integer_can_return_float():
    result = cal.subtract(2.0, 1)
    assert isinstance(result,float), "{} is not a float".format(result)
    assert result == 1.0

# multiplication
def test_multiply_two_integers_return_expected_value():
    assert cal.multiply(2,2) == 4

def test_multiply_integer_to_string_return_none():
    assert cal.multiply(1,'m') is None
    
def test_multiply_two_strings_return_none():
    assert cal.multiply('m','i') is None