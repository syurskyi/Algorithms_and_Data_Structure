#accept the number of inputs
for i in range(int(input())):
    
    #accept the three values S,R and P where S is current money R is the amount of money to be achieved and
    #P is the rate of interest
    a = list(map(int, input().split()))
    
    s,r,p = a
    year_count = 0
    while r >= s:
        #calculate the rate of interest on the amount and the numbers of years it will take to get the R
        s = s + (s*(p/100))
        year_count += 1
    print(year_count,end=' ')
        