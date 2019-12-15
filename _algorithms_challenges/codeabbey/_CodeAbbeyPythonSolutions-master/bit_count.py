amount_values = int(input())
results = []

def count(decimal_number):
    is_negative = False
    if(decimal_number < 0):
        decimal_number *= -1
        decimal_number -=1
        is_negative = True
    counter = 0
    while(decimal_number != 0):
        remainder = decimal_number%2
        if(remainder == 1):
            counter += 1
        decimal_number  //= 2

    if(is_negative):
        return 32-counter
    return counter

values = list(map(int, input().split()))
for i in range(amount_values):
    results.append(count(values[i]))

print(*results)