from functools import wraps


def make_html(element):
    def inner_func(func):
        @wraps(func, element)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'

        return wrapper

    return inner_func
