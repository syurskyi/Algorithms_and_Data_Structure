DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """

    def wrap(func):
        def wrapped(text, *args, **kwargs):
            _start = max(start, 0)
            _end = min(len(text), end) if end > 0 else 0
            result = (text[:_start], text[_start:_end], text[_end:])
            return func(f'{result[0]}{DOT * len(result[1])}{result[2]}')

        return wrapped

    return wrap
