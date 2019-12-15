from math import sqrt, floor

def prime(user_input):
    if user_input == 0 or user_input == 1:
        return False
    elif user_input == 2:
        return True
    elif user_input % 2 == 0:
        return False
    for divisor in list(range(3, floor(sqrt(user_input)) + 1, 2)):
        if user_input % divisor == 0:
            return False
    return True

user_input = int(input("enter a non-negative number: "))

if prime(user_input):
    print(str(user_input) + " is prime!")
else:
    print(str(user_input) + " is not prime!")
