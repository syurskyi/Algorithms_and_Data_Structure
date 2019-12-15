"""In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) according to the type of equality of the lists:

return SAME_REFERENCE if both lists reference the same object,
return SAME_ORDERED if they have the same content and order,
return SAME_UNORDERED if they have the same content unordered,
return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
and finally return NO_EQUALITY if none of the previous cases match."""

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