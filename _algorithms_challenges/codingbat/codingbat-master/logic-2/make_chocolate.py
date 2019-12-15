''' We want make a package of goal kilos of chocolate. We have small bars
(1 kilo each) and big bars (5 kilos each). Return the number of small bars to
use, assuming we always use big bars before small bars. Return -1 if it can't
be done. '''


def make_chocolate(small, big, goal):
    result = -1
    if small + big * 5 >= goal:
        big_needed = int(goal / 5)
        big_matched = big_needed if big_needed <= big else big
        if goal - big_matched * 5 <= small:
            result = goal - big_matched * 5
    return result
