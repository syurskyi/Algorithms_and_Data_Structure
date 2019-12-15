def sum_numbers(numbers=None):
    return sum(numbers if numbers is not None else range(101))
