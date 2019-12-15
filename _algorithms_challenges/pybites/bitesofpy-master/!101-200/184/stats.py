from collections import Counter
from csv import DictReader
from os import path
from urllib.request import urlretrieve

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(DATA) as d:
            return list(DictReader(d))

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    def _count_attribute(self, attrib, completed=False):
        return Counter(x[attrib] for x in self.rows if not completed or (completed and x['completed'] == 'True'))

    def _count_clicks(self, attrib, completed=False):
        counter = Counter()
        for x in self.rows:
            if not completed or (completed and x['completed'] == 'True'):
                counter[x[attrib]] += 1
        return counter

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(self._count_attribute('bite').items())

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(self._count_attribute('bite', True).items())

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(self._count_attribute('user').items())

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        return len(self._count_attribute('user', True).items())

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        return self._count_clicks('bite').most_common()[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        return self._count_clicks('user', True).most_common()[0][0]

