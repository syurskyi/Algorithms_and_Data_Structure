counter = {}

with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        category = line.split('/')[2]
        if category in counter:
            counter[category] += 1
        else:
            counter[category] = 1
        line = open_file.readline()

print(counter)
