
___ mySelectionSort(myarray
  print "myarray:",myarray
  ___ i __ r..(l..(myarray
    least _ i
    #print "outerloop:",myarray
    #print "I and Least element in outerloop:",i
    ___ k __ r..(i + 1 , l..(myarray
      #print "innerloop:",myarray
      #print "K:",k
      #print "comparing myarray[",k,"] with element at least pos myarray[",least,"]",myarray[k],myarray[least]
      __ myarray[k] < myarray[least]:
        #print "if",myarray[k],"<",myarray[least],"then least is changed from",least,"to",k
        least _ k

    #print "once we are out of inner for loop"
    #print "myarray[least] is swapped with myarray[i] i.e myarray[",least,"] is swapped with myarray[",i,"]",myarray[least],myarray[i]
    swap(myarray, least, i)
 
 
___ swap(myarray, x, y
  temp _ myarray[x]
  myarray[x] _ myarray[y]
  myarray[y] _ temp
	      
      
myarray_[500,400,300,200,100]
mySelectionSort(myarray)
print(myarray) 
