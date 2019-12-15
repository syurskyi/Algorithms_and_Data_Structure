import math as m

amount_values = int(input())
results = []

def get_index_of_fib_number(num):
    if(num == 0):
        return 0
    index = 2.078087 * m.log(num) + 1.672276
    return round(index)

for i in range(amount_values):
    results.append(get_index_of_fib_number(int(input())))

print(*results)





