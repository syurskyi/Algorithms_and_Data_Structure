
import sys
def gettwoelementsclosesttozero(myarray):
        print "Given Array:", myarray
        #print "Length of the Array:", len(myarray) 
	arrayLen = len(myarray)
	myarray.sort()
        #print "Array sorted:", myarray
	if(arrayLen < 2):
		#print "Invalid Input"
		return
	left = 0
	right = arrayLen - 1		
 	minimumLeft = left
	minimumRight = arrayLen - 1
	minimumSum = sys.maxint
	while(left < right):
                #print "start loop>>"
                #print "array:", myarray
		sum = myarray[left] + myarray[right];
                #print "Left index:", left
                #print "Right index:", right
                #print "Sum:", sum, "of", myarray[left],"+",myarray[right]
		if(abs(minimumSum) > abs(sum)):
			minimumSum = sum
			minimumLeft = left
			minimumRight = right
                        #print "Until now, the two elements ", myarray[minimumLeft], myarray[minimumRight], "whose sum", sum,"is minimum"

		if sum < 0:
			left += 1
                        #print "sum",sum,"is less then 0","move left index from",left-1,"to",left
		else: 
                      right -= 1
                      #print "sum",sum,"is more then 0","move right index from",right+1,"to",right
                #print "<< end loop"
	print "Finally, the two elements whose sum is minimum are ", myarray[minimumLeft], myarray[minimumRight]

myarray = [12, 70, -10, 50, -80, 85]
gettwoelementsclosesttozero(myarray)
