star_number = input("請輸入一連串小於10的正整數:\n")

number_list = []

for d in str(star_number):
    number_list.append(d)

print(number_list)
print()


star_matrix = [[' ' for i in range(len(number_list))] for i in range(9)]


for i in range(len(number_list)):           #輸入幾個數字
    for j in range(int(number_list[i])):    #印出該數字的星號數量
        star_matrix[int(j)][int(i)] = '*'


for row in star_matrix:
    print(row)



print()


count = 9
while count > 0:
    print(*star_matrix[count-1],sep=' ')
    count = count -1
    ## 顛倒著印，先印最後一行
    ## 印出陣列時不要有[ , ,]框框之類的，我搜尋了 python print list without brackets
    ## https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row
