amount_values = int(input())
results = []

def get_min(values):
    min = values[0]
    for i in values:
        if(i < min):
            min = i
        
    return min

for i in range(amount_values):
    values = list(map(int, input().split()))
    results.append(get_min(values))

print(*results)