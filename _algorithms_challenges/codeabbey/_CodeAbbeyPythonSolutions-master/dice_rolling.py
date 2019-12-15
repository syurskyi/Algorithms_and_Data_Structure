amount_values = int(input())
results = []

def get_dice_point(value):
    value = round(value*6+0.5)
    results.append(value)

for i in range(amount_values):
    value = float(input())
    get_dice_point(value)

print(*results)
