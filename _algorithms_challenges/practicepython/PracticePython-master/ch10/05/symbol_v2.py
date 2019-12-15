operation_symbol_dict={'+','-','*','/'}

symbol_dict={
'0':['0000','0  0','0  0','0  0','0000'],
'1':['  1 ',' 11 ','  1 ','  1 ',' 111'],
'2':[' 22 ','2  2','  2 ',' 2  ','2222'],
'3':['3333','   3',' 333','   3','3333'],
'4':['4  4','4  4','4444','   4','   4'],
'5':['5555','5   ','5555','   5','5555'],
'6':['6   ','6   ','6666','6  6','6666'],
'7':['7777','   7','  7 ',' 7  ','7   '],
'8':['8888','8  8','8888','8  8','8888'],
'9':['9999','9  9','9999','   9','9999'],
'+':['    ','  + ',' +++','  + ','    '],
'-':['    ','    ',' ---','    ','    '],
'*':['*  *',' ** ','****',' ** ','*  *'],
'/':['    ','   /','  / ',' /  ','/   '],
'=':['    ',' ===','    ',' ===','    ']
}



operation = input("請輸入一個四則運算，例如 50+8:\n")

operation_list = []

first_num = 0
second_num = 0
count = 0

## 切割運算式中的每個符號
for symbol in str(operation):
    
    operation_list.append(symbol)
    count = count +1

    if symbol in operation_symbol_dict:     ## 當讀取到的字元是運算符號
        operation_symbol = operation_list.pop(-1)   ## 把list最後一項(也就是運算符號)pop出來並存起來
        while len(operation_list) > 0:
            first_num = first_num * 10 + int(operation_list.pop(0))  ## 把list的最前面那項pop出來加到first number中
    
    if count == len(operation):
        while len(operation_list) > 0:      ## 當讀到最後一個字元
            second_num = second_num * 10 + int(operation_list.pop(0))## 把list的最前面那項pop出來加到second number中
        

print(first_num)
print(operation_symbol)
print(second_num)

## 現在能讀到兩個數字 以及運算符號
