from .main import fizzbuzz

def test_takes_number_return_string():
    assert isinstance(fizzbuzz(1), str)

def test_return_fizz_if_multiple_of_3():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(3) == "Fizz"

def test_return_buzz_if_multiple_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(100) == "Buzz"

def test_return_fizzbuzz_if_multiple_of_15():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(90) == "FizzBuzz"