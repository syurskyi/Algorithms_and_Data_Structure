solved = False
count = 0
while not solved:
    cal = input().split()
    if count == 0:
        res = int(cal[0])
        count = count + 1
        continue
    if cal[0] == '+':
        res += int(cal[1])
    elif cal[0] == '*':
        res *= int(cal[1])
    else:
        res = res % int(cal[1])
        solved = True
        print(res)