amount_values = int(input())
results = []

def avg(values):
    results.append(round(sum(values)/(len(values)-1)))


for i in range(amount_values):
    values = list(map(int, input().split()))
    avg(values)

print(*results)