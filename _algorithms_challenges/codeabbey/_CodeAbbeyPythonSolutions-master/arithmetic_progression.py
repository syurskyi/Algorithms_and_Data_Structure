amount_values = int(input())
results = []

def get_progression(start, inc, sum):
    progress = start
    for i in range(sum, 1,-1):
        start +=  inc
        progress += start
    results.append(progress)

for i in range(amount_values):
    start, inc, sum = map(int, input().split())
    get_progression(start,inc,sum)
print(*results)