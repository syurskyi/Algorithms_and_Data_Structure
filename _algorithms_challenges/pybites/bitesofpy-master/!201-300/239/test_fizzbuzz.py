from fizzbuzz import fizzbuzz

# write one or more pytest functions below, they need to start with test_
def test_fizzbuzz_base():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(6) == 'Fizz'

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(10) == 'Buzz'

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == 'Fizz Buzz'
    assert fizzbuzz(30) == 'Fizz Buzz'
