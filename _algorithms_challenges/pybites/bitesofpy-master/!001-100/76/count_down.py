from functools import singledispatch


@singledispatch
def count_down(data_type):
    d = ''
    try:
        if len(data_type) != 4:
            raise ValueError
        for i in data_type:
            d += f'{i}'
    except TypeError:
        raise ValueError
    for i in range(4, 0, -1):
        print(d[:i])


@count_down.register(int)
def _(data_type):
    while data_type > 0:
        print(data_type)
        data_type //= 10


@count_down.register(float)
def _(data_type: float):
    s = str(data_type)
    while s != '':
        print(s)
        s = s[:-1]
