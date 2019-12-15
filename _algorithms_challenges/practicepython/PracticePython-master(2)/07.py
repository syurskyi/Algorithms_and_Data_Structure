# List Comprehensions

# Given
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # New list with only even numbers
# for i in a:
#     if i % 2 == 0:
#         new_list.append(i)

# New list with only even numbers -- one line
print (list(i for i in a if i % 2 == 0))
