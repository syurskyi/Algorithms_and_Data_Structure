from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for a in args:
            if not isinstance(a, int):
                raise TypeError()
            if a < 0:
                raise ValueError()
        return func(*args, **kwargs)

    return wrapper
