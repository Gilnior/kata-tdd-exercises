from .main import add, ExceptionSeparatorAtTheEnd
import pytest

def test_takes_string_return_number():
    assert isinstance(add("0"), int)

def test_return_zero_if_empty_string():
    assert add("") == 0

def test_handling_one_number():
    assert add("99") == 99

def test_handling_two_numbers():
    assert add("99,1") == 100

def test_handling_three_numbers():
    assert add("1,2,3") == 6

def test_handling_new_line_as_separator():
    assert add("1\n2") == 3

def test_handling_new_line_and_comma_as_separators():
    assert add("3,3\n10") == 16

def test_error_if_separator_at_the_end():
    with pytest.raises(ExceptionSeparatorAtTheEnd):
        add("2,4,5\n")

def test_define_separator_at_the_start():
    assert add("//;\n1;2") == 3
    assert add("//sep\n2sep5") == 7
