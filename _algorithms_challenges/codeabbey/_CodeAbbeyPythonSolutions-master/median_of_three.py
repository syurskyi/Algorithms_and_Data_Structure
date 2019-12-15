amount_values = int(input())
results = []

def get_median(values):
    diff = []
    avg = int(sum(values)//len(values))
    for i in values:
        diff.append(abs(i-avg))
    
    med = values[diff.index(min(diff))]
    results.append(med)

for i in range(amount_values):
    valeus = list(map(int, input().split()))
    get_median(valeus)

print(*results)