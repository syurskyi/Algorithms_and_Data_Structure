
def myInsertionSort(myarray):
  print "myarray:",myarray
  for i in range(1, len(myarray)):
    tmp = myarray[i]
    k = i
    #print "in outer loop:",myarray
    #print "tmp:",tmp
    #print "k:",k
    while k > 0 and tmp < myarray[k - 1]:         
        #print k,"> 0 and",tmp,"<",myarray[k - 1],"so assigning myarray[k-1] to myarray[k] so myarray[",k,"] becomes myarray[",k-1,"]"
        myarray[k] = myarray[k - 1]
        k -= 1
        #print "in inner loop:",myarray
        #print "changed k from ",k+1,"to",k
    
    #print "once you are out of while loop: myarray[",k,"] contains",tmp
    myarray[k] = tmp    
      
myarray=[400,300,200,100]
myInsertionSort(myarray)
print(myarray) 
