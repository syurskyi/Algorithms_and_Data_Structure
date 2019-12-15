import random
import string
from datetime import datetime

class Robot:
    __name: str

    def __init__(self):
        self.__generate_new_name()

    @property
    def name(self):
        return self.__name

    def reset(self):
        self.__generate_new_name()

    def __generate_new_name(self):
        random.seed(datetime.timestamp(datetime.now()))
        brand = "".join(random.choices(string.ascii_uppercase, k=2))
        number = random.randrange(100, 999)
        self.__name = f"{brand}{number}"
