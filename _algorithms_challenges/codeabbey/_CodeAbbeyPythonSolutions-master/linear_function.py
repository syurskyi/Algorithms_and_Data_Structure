amount_values = int(input())
results = []

def get_slope_intercept(x1, y1, x2, y2):
    slope = int((y2-y1)/(x2-x1))
    intercept = (slope*x1-y1)*-1
    return "("+str(slope)+" "+str(intercept)+")"

for i in range(amount_values):
    x1,y1,x2,y2 = map(int, input().split())
    results.append(get_slope_intercept(x1,y1,x2,y2))

print(*results)