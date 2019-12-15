# List Overlap

# Given
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print list(set([i for i in a if i in b]))

# Solution 01
# for i1 in a:
#     if i1 in b:
#         new_list.append(i1)
#
# print new_list
