line_num = 0
char_num = 0

with open("./sample1.txt", "r+") as sample1:
    lines = sample1.readlines()
    for line in lines:
        line_num = line_num + 1
        for char in line:
            char_num = char_num + 1

print("行數:", line_num)
print("字數:", char_num)
