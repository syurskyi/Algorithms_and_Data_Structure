
___ myInsertionSort(myarray
  print "myarray:",myarray
  ___ i __ range(1, len(myarray)):
    tmp _ myarray[i]
    k _ i
    #print "in outer loop:",myarray
    #print "tmp:",tmp
    #print "k:",k
    _____ k > 0 and tmp < myarray[k - 1]:         
        #print k,"> 0 and",tmp,"<",myarray[k - 1],"so assigning myarray[k-1] to myarray[k] so myarray[",k,"] becomes myarray[",k-1,"]"
        myarray[k] _ myarray[k - 1]
        k -_ 1
        #print "in inner loop:",myarray
        #print "changed k from ",k+1,"to",k
    
    #print "once you are out of while loop: myarray[",k,"] contains",tmp
    myarray[k] _ tmp
      
myarray_[400,300,200,100]
myInsertionSort(myarray)
print(myarray) 
