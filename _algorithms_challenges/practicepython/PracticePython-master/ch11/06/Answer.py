N = int(input("將計算 1/2 + 1/2^2 + 1/2^3 + 1/2^4 + 1/2^5 + … + 1/2^N ，請輸入N的值:\n"))


def math(N):
    if N == 1:
        return 1/2
    return math(N-1)/2


## math(N)為第N項的值， 因為二冪次方的關係， 1 - 第N項值即為累加值
print(1-math(N))
