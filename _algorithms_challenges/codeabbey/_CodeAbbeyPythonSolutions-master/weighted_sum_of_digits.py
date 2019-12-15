amount_values = int(input())
results = []

def get_weight(num):
    len_of_num = len(str(num))
    weight_sum = 0
    for i in range(len_of_num, 0, -1):
        weight_sum += num%10*i
        num //= 10
    results.append(weight_sum)

values = list(map(int, input().split()))
for i in range(amount_values):
    get_weight(values[i])

print(*results)
