class Animal:
    # 'Class variables'
    _zoo = None
    _index = None

    def __init__(self, name: str):
        self.name = name.title()
        self.index = self._next_index()
        self._add_to_zoo(self)

    def __repr__(self):
        return f'{self.index}. {self.name}'

    @classmethod
    def _next_index(cls):
        if cls._index is None:
            cls._index = 10000
        cls._index += 1
        return cls._index

    @classmethod
    def _add_to_zoo(cls, animal):
        if cls._zoo is None:
            cls._zoo = []
        cls._zoo.append(animal)

    @classmethod
    def zoo(cls):
        if cls._zoo is None:
            return ''
        return str(cls._zoo)
