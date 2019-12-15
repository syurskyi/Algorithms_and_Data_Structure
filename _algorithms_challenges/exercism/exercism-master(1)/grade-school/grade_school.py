import collections

class School:
    def __init__(self):
        self._students = collections.defaultdict(list)

    def add_student(self, name, grade):
        self._students[grade].append(name)
        self._students[grade].sort()

    def roster(self):
        return [name for grade in sorted(self._students) for name in self._students[grade]]

    def grade(self, grade_number):
        return self._students.get(grade_number, [])
