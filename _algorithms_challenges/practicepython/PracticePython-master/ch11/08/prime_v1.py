def prime(N):
    for i in range(2,N-1):  ## 被 2 ~ N-1 的數字來除
        if N % i == 0:      ## 如果餘數為0表示 不是質數
            return False
    return True             ## 當被  2 ~ N-1 除之後都不能被整除，即為質數



for i in range(2,1001):
    print(i," : ",prime(i))
