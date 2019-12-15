ticket = input()

if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
    print(list('Счастливый'))
else:
    print(list(('Обычный')))
