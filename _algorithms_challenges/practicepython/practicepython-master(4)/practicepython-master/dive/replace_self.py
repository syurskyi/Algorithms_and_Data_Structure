class Men:
    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print("I'm a men! My name is " + self.name)

    def cast_to(self, sex, name):
        self.__class__ = sex
        self.name = name

    def method_unique_to_men(self):
        print('I made The Matrix')


class Women:
    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print("I'm a women! My name is " + self.name)

    def method_unique_to_women(self):
        print('I made Cloud Atlas')


men = Men('Larry')
men.who_are_you()
#>>> I'm a men! My name is Larry
men.method_unique_to_men()
#>>> I made The Matrix


men.cast_to(Women, 'Lana')
men.who_are_you()
#>>> I'm a women! My name is Lana
men.method_unique_to_women()
#>>> I made Cloud Atlas
