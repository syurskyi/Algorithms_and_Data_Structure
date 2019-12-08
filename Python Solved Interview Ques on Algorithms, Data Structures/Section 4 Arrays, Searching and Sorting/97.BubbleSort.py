def myBubbleSort(myArray):
    print "Given Array:",myArray
    for i in range(len(myArray)):
        #print "outer loop:",myArray
        #print "I index:",i
        for k in range(len(myArray) - 1, i, -1):
                #print "inner loop:",myArray
                #print "K index:",k 
                #print "comparing myArray[",k,"] with myArray[",k-1,"]",myArray[k],myArray[k-1]
                if (myArray[k] < myArray[k - 1]):
                    swap(myArray, k, k - 1)

def swap(myArray, x, y):
    tmp = myArray[x]
    myArray[x] = myArray[y]
    myArray[y] = tmp
      
myArray = [600,500,400,300,200,100]
myBubbleSort(myArray)
print(myArray)      
