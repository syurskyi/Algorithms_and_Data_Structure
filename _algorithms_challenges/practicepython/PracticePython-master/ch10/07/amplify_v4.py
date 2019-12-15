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

string = ""
input_digit = int(input("請輸入0~9: \n"))
print("\n\n\n")

matrix = [['*' for i in range ((2**input_digit -1)*4)] for i in range(input_digit*5)]

for term in range(input_digit+1):
    for i in range(5):
        for line_amplify in range(term):
            for j in range(4):  
                for char_amplify in range(term):  
                    matrix[(line_amplify) *5 +i][(2**(term-1)-1 ) * 4+ j * term + char_amplify ] = symbol_dict [str(input_digit)] [i][j]
                    string = string + symbol_dict [str(input_digit)] [i][j]
            print(string)
            string = ""
 

for row in matrix:
    print(*row, sep='')
