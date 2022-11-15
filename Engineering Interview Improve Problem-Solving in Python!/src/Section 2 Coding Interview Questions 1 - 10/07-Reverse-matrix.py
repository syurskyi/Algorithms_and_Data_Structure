#   [[1, 2]
#   [3, 4]
#   [5, 6]]
# OUTPUT
#   [[6, 5]
#   [4, 3]
#   [2, 1]]

def reverse_matrix(M):
    M.reverse()
    for row in M:
        row.reverse()

M = [[1, 2],
   [3, 4],
   [5, 6]]
reverse_matrix(M)
print(M)