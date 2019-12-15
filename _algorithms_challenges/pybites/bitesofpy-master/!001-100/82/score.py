from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f'{self.name} => {THUMBS_UP * self.value}'

    @classmethod
    def average(cls):
        return sum(v.value for v in list(cls))/len(cls)
