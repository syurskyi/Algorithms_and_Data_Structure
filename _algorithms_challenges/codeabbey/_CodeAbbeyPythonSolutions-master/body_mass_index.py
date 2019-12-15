amount_values = int(input())
results = []

def get_bmi(weight, height):
    return weight/height**2

for i in range(amount_values):
    weight, height = map(float, input().split())
    bmi = get_bmi(weight, height)
    if(bmi < 18.5):
        results.append("under")
    elif(bmi >= 18.5 and bmi < 25):
        results.append("normal")
    elif(bmi >= 25 and bmi < 30):
        results.append("over")
    else:
        results.append("obese")

print(*results)
