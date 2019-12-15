operation_symbol_dict={'+','-','*','/'}

symbol_dict={
'0':['0000','0  0','0  0','0  0','0000'],
'1':['  1 ',' 11 ','  1 ','  1 ',' 111'],
'2':[' 22 ','2  2','  2 ',' 2  ','2222'],
'3':['3333','   3',' 333','   3','3333'],
'4':['4  4','4  4','4444','   4','   4'],
'5':['5555','5   ','5555','   5','5555'],
'6':['6666','6   ','6666','6  6','6666'],
'7':['7777','   7','  7 ',' 7  ','7   '],
'8':['8888','8  8','8888','8  8','8888'],
'9':['9999','9  9','9999','   9','9999'],
'+':['    ','  + ',' +++','  + ','    '],
'-':['    ','    ',' ---','    ','    '],
'*':['*  *',' ** ','****',' ** ','*  *'],
'/':['    ','   /','  / ',' /  ','/   '],
'=':['    ',' ===','    ',' ===','    '],
'.':['    ','    ','    ',' .. ',' .. ']
}


operation = input("請輸入一個四則運算，例如 50+8:\n")

operation_list = []

first_num = 0
second_num = 0
answer_num = 0
count = 0

for symbol in operation:
    operation_list.append(symbol)
    count = count +1

    if symbol in operation_symbol_dict:
        operation_symbol = operation_list.pop(-1)
        while len(operation_list) > 0:
            first_num = first_num * 10 + int(operation_list.pop(0))
    
    if count == len(operation):
        while len(operation_list) > 0:
            second_num = second_num * 10 + int(operation_list.pop(0))

## 根據加減乘除的符號做運算
if operation_symbol == '+':
    answer_num = first_num + second_num
if operation_symbol == '-':
    answer_num = first_num - second_num
if operation_symbol == '*':
    answer_num = first_num * second_num
if operation_symbol == '/':
    answer_num = first_num / second_num
    


print(first_num, operation_symbol, second_num, '=', answer_num)


## 將原本的運算式 以及做完的運算結果及等號存入list
for symbol in operation:
    operation_list.append(symbol)
operation_list.append('=')
for symbol in str(answer_num):
    operation_list.append(symbol)

#print(operation_list)



operation_symbol_list_0 = []
operation_symbol_list_1 = []
operation_symbol_list_2 = []
operation_symbol_list_3 = []
operation_symbol_list_4 = []
## 這邊用5個list，每個lis儲存 運算式 "一行的符號" 
for symbol in operation_list:
    operation_symbol_list_0.append(symbol_dict [str(symbol)] [0])
    operation_symbol_list_1.append(symbol_dict [str(symbol)] [1])
    operation_symbol_list_2.append(symbol_dict [str(symbol)] [2])
    operation_symbol_list_3.append(symbol_dict [str(symbol)] [3])
    operation_symbol_list_4.append(symbol_dict [str(symbol)] [4])

print(*operation_symbol_list_0, sep=' ')
print(*operation_symbol_list_1, sep=' ')
print(*operation_symbol_list_2, sep=' ')
print(*operation_symbol_list_3, sep=' ')
print(*operation_symbol_list_4, sep=' ')



