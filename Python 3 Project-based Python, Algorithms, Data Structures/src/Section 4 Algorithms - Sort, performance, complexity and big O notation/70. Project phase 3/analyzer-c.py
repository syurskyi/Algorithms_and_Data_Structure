import time
import random
from demos import quicksort, mergesort

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

# For those of you who are familiar with list comprehension covered
# in section 3, the code in the function above can be written as below:

# def create_random_list(size, max_val):
#     return [random.randint(1,max_val) for num in range(size)]

size = int(input("What size list do you want to create? "))
max = int(input("What is the max value of the range? "))

l = create_random_list(size,max)
tic = time.time()
quicksort(l)
toc = time.time()
print("QS elapsed time -> ", toc-tic)
tic = time.time()
mergesort(l)
toc = time.time()
print("MS elapsed time -> ", toc-tic)
