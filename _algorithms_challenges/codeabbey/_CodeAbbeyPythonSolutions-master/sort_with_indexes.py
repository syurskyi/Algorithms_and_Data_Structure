amount_values = int(input())
results = []

def get_sorting_indexes(array):
    sorted_array = array.copy()
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if(sorted_array[j] > sorted_array[j+1]):
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]

    print(array)

    for i in sorted_array:
        results.append(array.index(i)+1)

array = list(map(int, input().split()))
get_sorting_indexes(array)

print(*results)
