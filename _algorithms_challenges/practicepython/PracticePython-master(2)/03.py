# List Less Than Ten

# List
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# New list with all elements <5
new_list = []

for i in a:
    if i < 5:
        new_list.append(i)

print new_list
