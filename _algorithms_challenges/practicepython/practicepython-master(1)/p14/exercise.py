import random
random.seed(0)

def removeDuplicates_iter(a):
    b = a
    for eleA in a:
        for eleB in b:
            if eleA == eleB:
                b.remove(eleA)
    return b

def removeDuplicates_sets(a):
    return list(set(a))

a = [int(1000*random.random()) for i in range(50)]

print(removeDuplicates_iter(a))

print(removeDuplicates_sets(a))
