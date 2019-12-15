amount_values = int(input())
results = []

def get_x_next(A,C,M,X0,N):
    if(N < 1):
        return X0
    x_next = (A*X0+C)%M
    return get_x_next(A,C,M, x_next, N-1)

for i in range(amount_values):
    A,C,M,X0,N = map(int, input().split())
    results.append(get_x_next(A,C,M,X0,N))

print(*results)
