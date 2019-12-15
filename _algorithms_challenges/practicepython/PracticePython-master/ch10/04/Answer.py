star_number = input("請輸入一連串小於10的正整數:\n")

number_list = []

for d in str(star_number):
    number_list.append(d)


star_matrix = [[' ' for i in range(len(number_list))] for i in range(9)]


for i in range(len(number_list)):           #輸入幾個數字
    for j in range(int(number_list[i])):    #印出該數字的星號數量
        star_matrix[int(j)][int(i)] = '*'

count = 9
while count > 0:
    print(*star_matrix[count-1],sep=' ')
    count = count -1


