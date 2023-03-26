def fizzbuzz(n):

    is_multiple_of_3 = n % 3 == 0 
    is_multiple_of_5 = n % 5 == 0 

    if is_multiple_of_3 and is_multiple_of_5:
        return "FizzBuzz"

    if is_multiple_of_3:
        return "Fizz"

    if is_multiple_of_5:
        return "Buzz"

    return str(n)