#n = 100
# 
import random
def print_random_del(l):
    for i in range(len(l),0,-1):
        index_to_delete = random.randint(0, i - 1)
        print(l[index_to_delete], index_to_delete)
        del l[index_to_delete]
        
def print_random(l):
    for i in range(len(l),0,-1):
        index_to_delete = random.randint(0, i - 1)
        print(l[index_to_delete], index_to_delete)
        l[index_to_delete] = l[i - 1]

print_random([1, 2, 7, 4,5, 6, 3])