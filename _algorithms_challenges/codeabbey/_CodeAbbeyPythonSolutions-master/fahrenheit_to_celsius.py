values = list(map(int, input().split()))
amount_values = values[0]
results = []

def convert_fahrenheit_to_celsius(fahrenheit_degree):
    celsius_degree = round((fahrenheit_degree-32)/1.8)
    return celsius_degree

for i in range(1,amount_values+1):
    results.append(convert_fahrenheit_to_celsius(values[i]))

print(*results)