#Ask for how number to be entered
data = int(input())
result = 0
arr = []

while len(arr) < data:
    arr = input().split()
    #print('length of arr is:', len(arr))
    #print('values is in arr are :', arr)
    
    #traversing through each element of the array
    for x in range(len(arr)):
        
        #print('current array is :', currarr)
        result =  (result + int(arr[x])) * 113
        #print('result of calculation of ',arr[x],' is : ',result)
        if result > 10000007:
            #print('result is greater than 10000007 for ',arr[x],' thus iam performing mod')
            result = result % 10000007
            #print('mod result is: ',result)
#print the result
print(result)