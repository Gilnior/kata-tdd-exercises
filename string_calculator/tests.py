from .main import add

def test_takes_string_return_number():
    assert isinstance(add("0"), int)
