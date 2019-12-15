symbol_dict={
'0':['****','*  *','*  *','*  *','****'],
'1':['  * ',' ** ','  * ','  * ',' ***'],
'2':[' ** ','*  *','  * ',' *  ','****'],
'3':['****','   *',' ***','   *','****'],
'4':['*  *','*  *','****','   *','   *'],
'5':['****','*   ','****','   *','****'],
'6':['****','*   ','****','*  *','****'],
'7':['****','   *','  * ',' *  ','*   '],
'8':['****','*  *','****','*  *','****'],
'9':['****','*  *','****','   *','****']
}


number = input("請輸入任一正整數:\n")

number_list = []

for symbol in number:
    number_list.append(symbol)

number_symbol_list_0 = []
number_symbol_list_1 = []
number_symbol_list_2 = []
number_symbol_list_3 = []
number_symbol_list_4 = []
## 這邊用5個list，每個lis儲存 運算式 "一行的符號" 
for symbol in number_list:
    number_symbol_list_0.append(symbol_dict [str(symbol)] [0])
    number_symbol_list_1.append(symbol_dict [str(symbol)] [1])
    number_symbol_list_2.append(symbol_dict [str(symbol)] [2])
    number_symbol_list_3.append(symbol_dict [str(symbol)] [3])
    number_symbol_list_4.append(symbol_dict [str(symbol)] [4])

print(*number_symbol_list_0, sep=' ')
print(*number_symbol_list_1, sep=' ')
print(*number_symbol_list_2, sep=' ')
print(*number_symbol_list_3, sep=' ')
print(*number_symbol_list_4, sep=' ')
