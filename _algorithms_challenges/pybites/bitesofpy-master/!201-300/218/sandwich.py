from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        print(UPPER_SLICE)
        func(*args, **kwargs)
        print(LOWER_SLICE)

    return wrapped
