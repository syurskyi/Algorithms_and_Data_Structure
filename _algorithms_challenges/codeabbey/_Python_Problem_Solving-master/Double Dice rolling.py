#accept the range
for i in range(int(input())):
    #accept the random numbers to be converted to double dice value
    a,b = list(map(int,input().split()))
    #calculate the double dice value
    res = (a % 6 + 1 ) + (b % 6 + 1)
    #print the result
    print(res,end=' ')