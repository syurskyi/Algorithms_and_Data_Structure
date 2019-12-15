RESERVED_WORDS = vars(object).keys()


class JsObject:
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """

    def __init__(self, **kwargs):
        self._local = dict()
        for k, v in kwargs.items():
            self.__setitem__(k, v)

    def __getattr__(self, item):
        if item in self.keys():
            return self.__getitem__(item)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key not in RESERVED_WORDS and key != '_local':
            self._local[key] = value

    def __getitem__(self, item):
        return self._local.get(item)

    def __setitem__(self, key, value):
        if key not in RESERVED_WORDS:
            self._local[key] = value
            self.__dict__[key] = value
        else:
            raise AttributeError("Reserved words not allowed")

    def __delitem__(self, key):
        self._local.pop(key)
        self.__dict__.pop(key)

    def __delattr__(self, item):
        self._local.pop(item)
        self.__dict__.pop(item)

    def __len__(self):
        return len(self._local)

    def __iter__(self):
        yield from self._local

    def __eq__(self, other):
        return self._local == other._local

    def keys(self):
        return self._local.keys()

    def values(self):
        return self._local.values()

    def update(self, data):
        for k, v in data.items():
            self.__setitem__(k, v)
