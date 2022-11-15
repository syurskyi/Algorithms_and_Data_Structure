# input = [1, 2, 1, 4, 5, 6, 6] ... output [1,2,4,5,6]

def remove_duplicates(l):# worst case [1,2,4,5,6]
    result = {}
    for val in l: # n times
        if not val in result: # 1, 2, 3, 4 ... n - 1 # Balanced tree as a result  we would get n * log n
            result[val] = 1 #(n * n - 1) /2 = O(n squared)
    return list(result.keys()) # n times 1 (dont count colisions)

print(remove_duplicates([1, 2, 1, 4, 5, 6, 6]))
    