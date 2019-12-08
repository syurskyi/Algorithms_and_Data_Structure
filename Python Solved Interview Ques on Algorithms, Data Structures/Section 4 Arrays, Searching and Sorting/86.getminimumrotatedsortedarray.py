
def getMinVal(myarray):
        print "given array:",myarray
        midindex, lowerindex, highindex = 0, 0, len(myarray) - 1
        while myarray[lowerindex] >= myarray[highindex]:
            #print "start loop >>",myarray 
            #print "highindex",highindex
            #print "lowerindex",lowerindex
            if highindex - lowerindex <= 1:
                print "minimum value is:", myarray[highindex],"pos is:", highindex 
                return myarray[highindex], highindex
            midindex = (lowerindex + highindex)/2 
            #print "midindex",midindex,"is","(",lowerindex,"+",highindex,")","right shifted to 1, so midindex is",midindex
            #print "myarray[midindex] myarray[",midindex,"]",myarray[midindex]
            #print "myarray[lowerindex] myarray[",lowerindex,"]",myarray[lowerindex]
            #print "myarray[highindex] myarray[",highindex,"]",myarray[highindex]
            if myarray[midindex] == myarray[lowerindex]:
                lowerindex += 1
                #print "myarray[midindex] is equal to myarray[lowerindex]",myarray[midindex],"is equal to",myarray[lowerindex-1],"so lowerindex value changed from",lowerindex-1,"to",lowerindex
            elif myarray[midindex] > myarray[lowerindex]:
                temp = lowerindex
                lowerindex = midindex
                #print "myarray[midindex] is greater then myarray[lowerindex]",myarray[midindex],"is greater then",myarray[temp],"so lowerindex value changed to midindex",midindex
            elif myarray[midindex] == myarray[highindex]:
                highindex -= 1
                #print "myarray[midindex] is equal then myarray[highindex]",myarray[midindex],"is equal to",myarray[highindex],"so highindex changed from",highindex+1,"to",highindex
            else:
                temp = highindex
                highindex = midindex
                #print "myarray[midindex] is not equal to myarray[highindex]",myarray[midindex],"is not equal to",myarray[temp],"so highindex changed to midindex",midindex
            #print "<< end loop"
        print "minimum value is:", myarray[lowerindex],"pos is:",lowerindex
        return myarray[lowerindex], lowerindex

myarray=[10,11,12,13,1,2,3,4,5]	
getMinVal(myarray)
