a = [
    [18, -51, 23] ,
    [35, 10, 9],
    [-3, 52, 81],
    [69, 88, 20]
    ]

b = [
    [28, 32, -35],
    [40, 73, 17],
    [92, 32, 13],
    [29, 38, 10]
    ]

def matrix_add(matrix_a, matrix_b):
    matrix_result = [[0 for i in range(3)] for i in range(4)]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return matrix_result


result = matrix_add(a, b)

for row in result:
    print(row)
