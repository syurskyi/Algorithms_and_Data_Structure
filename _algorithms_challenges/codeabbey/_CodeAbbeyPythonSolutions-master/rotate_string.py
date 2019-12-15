amount_values = int(input())
results = []

def rotate(index, string):
    sub_string1 = string[:index]
    sub_string2 = string[index:]

    rotated_string = sub_string2+sub_string1
    return rotated_string

for i in range(amount_values):
    index, string = map(str, input().split())
    index = int(index)
    results.append(rotate(index, string))

print(*results)