amount_value = int(input())
results = []

def get_dice_point(dice1, dice2):
    point = (dice1%6+1)+(dice2%6+1)
    return point

for i in range(amount_value):
    dice1, dice2 = map(int, input().split())
    results.append(get_dice_point(dice1, dice2))

print(*results)
