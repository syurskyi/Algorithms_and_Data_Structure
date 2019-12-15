import random

bingo = [i for i in range(16)]
random.shuffle(bingo)   #將排序打亂

print(bingo)

bingo_4x4 = [['*' for i in range(4)]for i in range(4)]

for row in bingo_4x4:
    print(row)
