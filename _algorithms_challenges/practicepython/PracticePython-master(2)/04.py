# Divisors

num = int(input("Give me a number between 2-100: "))

# list of numbers 1-100
old_list = range(2, 100)
new_list = []

for i in old_list:
    if num % i == 0:
        new_list.append(i)

print (new_list)
