amount_value = int(input())

generator_list = []
results = []

def generate(num, counter):
    
    if(num in generator_list):
        return counter
    generator_list.append(num)
    num **= 2
    num = (num//100)%10000
    return generate(num, counter+1)

values = list(map(int, input().split()))

for i in range(amount_value):
    results.append(generate(values[i],0))
    generator_list.clear()

print(*results)