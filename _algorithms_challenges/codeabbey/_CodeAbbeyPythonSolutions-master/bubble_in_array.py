def get_checksum(values):
    limit = 10000007
    result = 0
    seed = 113

    for i in values:
        result = (result + i) * seed
        if(result > limit):
            result = result % limit

    return result

def get_swap_number(array):

    swapped = 0

    n = len(array)
    for i in range(n-1):
        if(array[i] > array[i+1]):
            swapped += 1
            array[i], array[i+1] = array[i+1], array[i]
    return swapped

array = list(map(int, input().split()))[:-1]

print(get_swap_number(array), get_checksum(array))