from enum import Enum
import collections

class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):

    if list1 is list2:
        return Equality(4)
    elif list1 == list2:
        return Equality(3)
    elif collections.Counter(list1) == collections.Counter(list2):
        return Equality(2)
    elif set(list1) == set(list2) and list1 not in list2:
        return Equality(1)
    else:
        return Equality(0)
