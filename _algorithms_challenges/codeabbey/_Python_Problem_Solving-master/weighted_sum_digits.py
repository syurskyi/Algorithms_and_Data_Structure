#ask user for number of records
data = int(input())
result = []
#run the following logic while list result is less than data
while len(result) < data:
    #split all the records so that it can be accessed differently
    num = input().split()
    for i in range(0,len(num)):
        
        digitsum = 0
        #take data individually to perform weighted sum
        currnum = num[i]
        
        #get the length of the current weighted sum
        for j in range(1,len(currnum)+1):
            #calculate the sum
            digitsum +=j * int(currnum[j-1])
        #appending the result to the result list
        result.append(digitsum)

#displaying the records
for i in result:
    print(i,end=(' '))