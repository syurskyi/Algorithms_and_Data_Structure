scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt_number = None

    @property
    def _last_earned_belt(self):
        """Return the name of the currently qualified belt, if no belt has been awarded None is returned"""
        return ranks[self._last_earned_belt_number] if self._last_earned_belt_number is not None else None

    @staticmethod
    def _get_belt(new_score):
        """Find the index number of the belt for the provide score"""
        return len([x for x in scores if x <= new_score]) - 1

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        """
        Set the current score and update any belt qualification
        new_score must be an integer and cannot be less than the current score
        """
        if not isinstance(new_score, int):
            raise ValueError('Score can only be an integer')
        if self._score > new_score:
            raise ValueError(f'New score ({new_score}) must be higher than previous score ({self._score})')
        self._score = new_score
        belt = self._get_belt(new_score)
        if self._last_earned_belt is None or self._last_earned_belt_number < belt:
            self._last_earned_belt_number = belt
            print(f'Congrats, you earned {new_score} points obtaining the PyBites Ninja '
                  f'{self._last_earned_belt.title()} Belt')
        else:
            print(f'Set new score to {new_score}')

    score = property(_get_score, _set_score)
