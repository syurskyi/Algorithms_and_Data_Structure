#number of measurements to inserted
data = int(input())
#enter all the measurements seperated by space
mea = list(map(float, input().split()))
#this array is used to store the results
mea_store = []

#traversing through each element of the measurements
for i in range(len(mea)):
    #if first element then store it in the result
    if i == 0:
        mea_store.append(mea[i])
    #if last element then store it in the result array
    elif i== len(mea)-1:
        mea_store.append(mea[i])
        break
    #else calculate the average of the middle numbers and store in the result
    else:
        res = (mea[i]+mea[i-1]+mea[i+1])/3
        mea_store.append(res)
        
#printing the values 
for i in mea_store:
    print(i,end=' ')
    