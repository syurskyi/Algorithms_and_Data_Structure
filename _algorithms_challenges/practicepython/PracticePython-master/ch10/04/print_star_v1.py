star_number = input("請輸入一連串小於10的正整數:\n")

number_list = []



## 像這裡要輸入一連串數字 首先要切割每個數字，想辦法存到陣列裡 
## 我會查關鍵字 python split digit
## https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python

for d in str(star_number):
    number_list.append(d)

print(number_list)
print()



## 這裡我想宣告一個空白二維陣列，存放所有星星
## 二維陣列宣告方法 搜尋 python 2 dimensional list declaration
## https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python

star_matrix = [['' for i in range(9)] for i in range(len(number_list))]


for i in range(len(number_list)):           #輸入幾個數字 就迴圈幾次
    for j in range(int(number_list[i])):    #印出該數字的星號數量(迴圈存星星)
        star_matrix[int(i)][int(j)] = '*'


for row in star_matrix:
    print(row)

## 印出來發現跟想像的不太一樣，是行列顛倒的問題
## 所以在二版裡，我把 宣告二維陣列 以及 存放星星的[][]兩個地方 方框框裡面的變數做了交換
