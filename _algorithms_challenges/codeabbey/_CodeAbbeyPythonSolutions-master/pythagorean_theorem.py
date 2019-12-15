import math

amount_values = int(input())
results = []

def get_triangle_type(side1, side2, side3):
    hypotenuse = math.sqrt(side1**2 + side2**2)
    if(side3 < hypotenuse):
        return "A"
    elif(side3 > hypotenuse):
        return "O"
    else:
        return "R"

for i in range(amount_values):
    side1, side2, side3 = map(int, input().split())
    results.append(get_triangle_type(side1,side2, side3))

print(*results)