# see __mro__ output in Bite description

class Person(object):
    def __repr__(self):
        return 'I am a person'


class Father(Person):
    def __repr__(self):
        return f'{super().__repr__()} and cool daddy'


class Mother(Person):
    def __repr__(self):
        return f'{super().__repr__()} and awesome mom'


class Child(Father, Mother, Person):
    def __repr__(self):
        return 'I am the coolest kid'
