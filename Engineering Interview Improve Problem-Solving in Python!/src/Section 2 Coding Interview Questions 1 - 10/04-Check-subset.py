# [1, 2, 4, 7, "a"] [" b", "a", 1, 2, 7, 3, 4] = true

def is_subset(L1, L2):
    temp = dict([(e, 1) for e in L2])
    for e in L1: #n 
        if not e in temp: # n n  
            return False
    return True

print(is_subset([1, 2, 4, 7, "c"], [" b", "a", 1, 2, 7, 3, 4]))