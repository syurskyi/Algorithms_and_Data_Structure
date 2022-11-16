___ myBubbleSort(myArray
    print "Given Array:",myArray
    ___ i __ r..(l..(myArray
        #print "outer loop:",myArray
        #print "I index:",i
        ___ k __ r..(l..(myArray) - 1, i, -1
                #print "inner loop:",myArray
                #print "K index:",k 
                #print "comparing myArray[",k,"] with myArray[",k-1,"]",myArray[k],myArray[k-1]
                __ (myArray[k] < myArray[k - 1]
                    swap(myArray, k, k - 1)

___ swap(myArray, x, y
    tmp _ myArray[x]
    myArray[x] _ myArray[y]
    myArray[y] _ tmp
      
myArray _ [600,500,400,300,200,100]
myBubbleSort(myArray)
print(myArray)      
