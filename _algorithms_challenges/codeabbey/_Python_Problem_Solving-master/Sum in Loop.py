Num = int(input())
listo = []
while len(listo) < Num:
    number = input()
    listo = number.split()
result = 0
for i in listo:
    result = result + int(i)
print(result)