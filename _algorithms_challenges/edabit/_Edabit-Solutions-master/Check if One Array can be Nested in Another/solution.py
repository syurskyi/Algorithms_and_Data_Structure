def can_nest(list1, list2):
    list1.sort()
    list2.sort()
    if list1[0] > list2[0] and list1[-1] < list2[-1]:
        return True
    else:
        return False
