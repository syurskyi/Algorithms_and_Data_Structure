"""
In this Bite you calculate the total amount of points earned with Ninja Belts by accessing the given ninja_belts dict.

You learn how to access score and ninjas (= amount of belt owners) from no less than a namedtuple.

Why a namedtuple, you did not even mention a tuple yet?!

Good point, well in our Bites we might actually use them even more so let's get to know them here (if you have a free evening read up on the collections module as well and thank us later).

The function returns the total score int. You learn to write generic code because we test for an updated ninja_belts dict as well, see the TESTS tab.
"""
from collections import namedtuple

# Car = namedtuple('Car', ['color', 'mileadge'])
# my_car = Car('blue', 150000)
# print(my_car)

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
    total_scores = []
    
    for i in belts:
        total_scores.append(int(belts[i].score * belts[i].ninjas))
        
    return sum(total_scores)


get_total_points()
