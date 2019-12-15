import random

bingo = [i for i in range(16)]
random.shuffle(bingo)   #將排序打亂

bingo_4x4 = [[bingo[i + 4 * j] for i in range(4)]for j in range(4)]

for row in bingo_4x4:
    print(row)

print()

print("這是一個 4 X 4 賓果遊戲，")
for i in range(16):
    input_num = int(input("請輸入1~16的數字: "))
    for index in range(16):
        if input_num == bingo[index]:
            row = index // 4
            col = index % 4
            print("第", index, "項    在", row, "列", col, "行")
            
