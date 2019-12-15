#run the for loop for the number of elements
for i in range(int(input())):
    
    #accept the value of a,c,m,x,n in a list
    listo = list(map(int,input().split()))
    
    #assign the list to variables
    a,c,m,x,n = listo
    
    #run the loop to get the value of the nth number
    for j in range(n):
        x = (a*x + c) % m
        
    #print the output
    print(x,end = ' ')