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
'9':['9999','9  9','9999','   9','9999']
}


input_digit = input("請輸入0~9: \n")
print("\n\n\n")

for i in range(int(input_digit)):
    for j in range(int(input_digit)):
        print(symbol_dict [str(input_digit)] [0], sep='')
    for j in range(int(input_digit)):
        print(symbol_dict [str(input_digit)] [1], sep='')
    for j in range(int(input_digit)):
        print(symbol_dict [str(input_digit)] [2], sep='')
    for j in range(int(input_digit)):
        print(symbol_dict [str(input_digit)] [3], sep='')
    for j in range(int(input_digit)):
        print(symbol_dict [str(input_digit)] [4], sep='')

## 倍數方法印出，將每行每列都放大N倍
## 但結果還不是想要的
