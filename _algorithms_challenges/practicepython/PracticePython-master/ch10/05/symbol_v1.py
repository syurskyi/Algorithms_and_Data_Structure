## 原先那支程式的冒號打成中文的冒號了(雖然是半形 但不通用)

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

## 將乘法x改成*字號

def print_symbol(symbol_dict):
    
    return symbol_dict[0]+'\n'+symbol_dict[1]+'\n'+symbol_dict[2]+'\n'+symbol_dict[3]+'\n'+symbol_dict[4]

print(print_symbol(symbol_dict['0']))
print(print_symbol(symbol_dict['1']))
print(print_symbol(symbol_dict['2']))
print(print_symbol(symbol_dict['3']))
print(print_symbol(symbol_dict['4']))
print(print_symbol(symbol_dict['5']))
print(print_symbol(symbol_dict['6']))
print(print_symbol(symbol_dict['7']))
print(print_symbol(symbol_dict['8']))
print(print_symbol(symbol_dict['9']))
print(print_symbol(symbol_dict['+']))
print(print_symbol(symbol_dict['-']))
print(print_symbol(symbol_dict['*']))
print(print_symbol(symbol_dict['/']))
print(print_symbol(symbol_dict['=']))

## 確認所有符號印出來沒有問題
