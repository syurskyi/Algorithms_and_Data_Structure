def get_safe_position(N,K):
    safe_position = 0
    for i in range(1,N+1):
        safe_position = (safe_position+K) % i
    return safe_position+1

N,K = map(int, input().split())

print(get_safe_position(N,K))