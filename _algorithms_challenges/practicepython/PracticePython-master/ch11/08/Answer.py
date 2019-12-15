import math

def prime(N):   ## 其實只要判斷 2 ~ √N 的數就能知道是否為質數了
    for i in range(2, int(math.sqrt(N)+1)):
        if N % i == 0:
            return False
    return True



for i in range(2,1001):
    print(i," : ",prime(i))
