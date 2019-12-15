MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        if any((birthday.day == x.day and birthday.month == x.month) for (_, x) in self.items()):
            print(MSG.format(name))
        dict.__setitem__(self, name, birthday)
