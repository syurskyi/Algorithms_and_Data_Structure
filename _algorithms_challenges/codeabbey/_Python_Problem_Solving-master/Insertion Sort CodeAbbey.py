a = input()
x = list(map(int, input().split()))

temp = 0
temp_ind = []

# traversing through all the elements of the list expect first.
for i in range(1,len(x)):
    #storing the current element in the temp variable 
    #to compare with element which are sorted
    temp = x[i]
    temp_i = i
    count = 0
    #traverse through the elements which are sorted backwards
    for j in range(i-1,-1,-1):
        #if the temp element is smaller than the sorted number swap them 
        #and see if the n-1 is small or big and continue
        if temp < x[j]:
            #print('\n comparing',temp,x[j])
            x[temp_i],x[j] = x[j],temp
            #decrement the temp_i to traverse backward
            temp_i -= 1
            count += 1
    print(count,end =' ')
    
#print('\n',x)