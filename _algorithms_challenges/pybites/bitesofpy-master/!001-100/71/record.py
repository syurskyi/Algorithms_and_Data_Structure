from pprint import pprint


class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max = 0

    def __call__(self, *args, **kwargs):
        if self.max < args[0]:
            self.max = args[0]
        return self.max

