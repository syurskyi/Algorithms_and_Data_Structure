values = []
line = ""
strValues = ""
result = 0

while True:
    line = input()
    if(line):
        values.append(line.replace(" ", ""))
    else:
        break
mod = int(values[len(values)-1][1:])

for i in values:
    strValues += i
    result = eval(strValues)%mod
    strValues = str(result)

print(result)