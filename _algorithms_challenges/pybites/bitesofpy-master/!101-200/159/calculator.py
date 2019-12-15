from operator import add, sub, mul, truediv


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,
    """
    funcs = {'+': add, '-': sub, '*': mul, '/': truediv}
    try:
        a, op, b = calculation.split()
        a, b = int(a), int(b)
        return funcs[op](a, b)
    except Exception:
        raise ValueError
