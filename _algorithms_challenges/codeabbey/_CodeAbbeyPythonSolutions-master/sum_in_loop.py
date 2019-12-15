amount_values = int(input())
values = list(map(int, input().split()))

def get_sum():

    result = 0
    for i in values:
        result = result + i

    return result

print(get_sum())