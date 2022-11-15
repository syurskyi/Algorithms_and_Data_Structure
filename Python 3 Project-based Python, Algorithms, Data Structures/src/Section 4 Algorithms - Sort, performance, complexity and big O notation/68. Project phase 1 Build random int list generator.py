import random
import demos

def create_random_list(size, max_val):
    ran_list = []
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

# For those of you who are familiar with list comprehension covered
# in section 3, the code in the function above can be written as below:

# def create_random_list(size, max_val):
#     return [random.randint(1,max_val) for num in range(size)]

print(create_random_list(100,100))
