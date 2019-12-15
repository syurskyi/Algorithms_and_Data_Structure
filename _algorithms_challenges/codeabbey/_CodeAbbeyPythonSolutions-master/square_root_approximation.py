amount_values = int(input())
results = []

def get_sqrt(num, r, step):
    d = num/r
    if(step == 0):
        return round(r,7)
    else:
        r = (r+d)/2
        return get_sqrt(num,r,step-1)
        
for i in range(amount_values):
    r = 1
    num, step = map(int, input().split())
    results.append(get_sqrt(num,r,step))

print(*results)