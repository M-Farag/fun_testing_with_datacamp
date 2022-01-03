import pytest
import calculator as cal


class TestAdd(object):
    # ADD
    def test_add_two_numbers(self):
        assert cal.add(1,1) == 2

    def test_add_two_strings_return_exception_type_error(self):
        with pytest.raises(TypeError) as exception_info:
            cal.add('a','b')

    def test_add_integer_to_string_return_none(self):
        with pytest.raises(TypeError) as exception_info:
            cal.add(1,'a')
        assert exception_info.match('You cannot add strings')

# Subtract
class TestSubtract(object):
    def test_subtract_two_integers_return_integer(self):
        results = cal.subtract(2,1)
        assert isinstance(results,int),"{} is not an integer".format(results)
        assert  results == 1

    def test_subtract_two_strings_return_none(self):
        assert cal.subtract('a','b') is None

    def test_subtract_integer_and_string_return_none(self):
        assert cal.subtract(1,'n') is None

    def test_subtract_two_integers_can_return_negative_value(self):
        assert cal.subtract(2,3) == -1

    def test_subtract_float_and_integer_can_return_float(self):
        result = cal.subtract(2.0, 1)
        assert isinstance(result,float), "{} is not a float".format(result)
        assert result == 1.0

# multiplication
class TestMultiply(object):
    def test_multiply_two_integers_return_expected_value(self):
        assert cal.multiply(2,2) == 4

    def test_multiply_integer_to_string_return_none(self):
        assert cal.multiply(1,'m') is None
        
    def test_multiply_two_strings_return_none(self):
        assert cal.multiply('m','i') is None