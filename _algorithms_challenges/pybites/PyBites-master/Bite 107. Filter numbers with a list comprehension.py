"""
Complete the function below that receives a list of numbers and returns only the even numbers that are > 0 and even (divisible by 2).

The challenge here is to use Python's elegant list comprehension feature to return this with one line of code (while writing readable code).

"""

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    return [n for n in numbers if n > 0 and n % 2 == 0]
