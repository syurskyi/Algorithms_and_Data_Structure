amount_values = int(input())
results = []

def get_area(x1, y1, x2, y2, x3, y3):
    return (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2


for i in range(amount_values):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    area_of_triangle = get_area(x1,y1,x2,y2,x3,y3)

    if(area_of_triangle < 0):
        area_of_triangle *= -1
    results.append(area_of_triangle)

print(*results)

