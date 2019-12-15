string_data = input().split()
print(string_data)
result = []
for i in range(len(string_data)):
    str = string_data[i]
    str = str[::-1]
    result.append(str)

result = result[::-1]

for j in result:
    print(j,end=(' '))
    