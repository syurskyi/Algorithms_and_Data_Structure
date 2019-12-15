amount_values = int(input())
results = []

def is_triangle(sides):
    if(sides[0] + sides[1] < sides[2]):
        return 0
    elif(sides[1] + sides[2] < sides[0]):
        return 0
    elif(sides[0] + sides[2] < sides[1]):
        return 0
    else:
        return 1

for i in range(amount_values):
    sides = list(map(int, input().split()))
    results.append(is_triangle(sides))

print(*results)

