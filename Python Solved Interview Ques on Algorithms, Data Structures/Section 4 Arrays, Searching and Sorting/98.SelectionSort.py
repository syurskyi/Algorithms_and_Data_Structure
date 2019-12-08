
def mySelectionSort(myarray):
  print "myarray:",myarray
  for i in range(len(myarray)):
    least = i
    #print "outerloop:",myarray
    #print "I and Least element in outerloop:",i
    for k in range(i + 1 , len(myarray)):
      #print "innerloop:",myarray
      #print "K:",k
      #print "comparing myarray[",k,"] with element at least pos myarray[",least,"]",myarray[k],myarray[least]
      if myarray[k] < myarray[least]:
        #print "if",myarray[k],"<",myarray[least],"then least is changed from",least,"to",k
        least = k

    #print "once we are out of inner for loop"
    #print "myarray[least] is swapped with myarray[i] i.e myarray[",least,"] is swapped with myarray[",i,"]",myarray[least],myarray[i]
    swap(myarray, least, i)
 
 
def swap(myarray, x, y):
  temp = myarray[x]
  myarray[x] = myarray[y]
  myarray[y] = temp
	      
      
myarray=[500,400,300,200,100]
mySelectionSort(myarray)
print(myarray) 
