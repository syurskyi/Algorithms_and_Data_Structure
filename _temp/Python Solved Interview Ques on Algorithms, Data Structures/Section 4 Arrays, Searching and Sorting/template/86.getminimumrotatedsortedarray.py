
___ getMinVal(myarray
        print "given array:",myarray
        midindex, lowerindex, highindex _ 0, 0, len(myarray) - 1
        _____ myarray[lowerindex] >_ myarray[highindex]:
            #print "start loop >>",myarray 
            #print "highindex",highindex
            #print "lowerindex",lowerindex
            __ highindex - lowerindex <_ 1:
                print "minimum value is:", myarray[highindex],"pos is:", highindex 
                r_ myarray[highindex], highindex
            midindex _ (lowerindex + highindex)/2
            #print "midindex",midindex,"is","(",lowerindex,"+",highindex,")","right shifted to 1, so midindex is",midindex
            #print "myarray[midindex] myarray[",midindex,"]",myarray[midindex]
            #print "myarray[lowerindex] myarray[",lowerindex,"]",myarray[lowerindex]
            #print "myarray[highindex] myarray[",highindex,"]",myarray[highindex]
            __ myarray[midindex] == myarray[lowerindex]:
                lowerindex +_ 1
                #print "myarray[midindex] is equal to myarray[lowerindex]",myarray[midindex],"is equal to",myarray[lowerindex-1],"so lowerindex value changed from",lowerindex-1,"to",lowerindex
            elif myarray[midindex] > myarray[lowerindex]:
                temp _ lowerindex
                lowerindex _ midindex
                #print "myarray[midindex] is greater then myarray[lowerindex]",myarray[midindex],"is greater then",myarray[temp],"so lowerindex value changed to midindex",midindex
            elif myarray[midindex] == myarray[highindex]:
                highindex -_ 1
                #print "myarray[midindex] is equal then myarray[highindex]",myarray[midindex],"is equal to",myarray[highindex],"so highindex changed from",highindex+1,"to",highindex
            ____
                temp _ highindex
                highindex _ midindex
                #print "myarray[midindex] is not equal to myarray[highindex]",myarray[midindex],"is not equal to",myarray[temp],"so highindex changed to midindex",midindex
            #print "<< end loop"
        print "minimum value is:", myarray[lowerindex],"pos is:",lowerindex
        r_ myarray[lowerindex], lowerindex

myarray_[10,11,12,13,1,2,3,4,5]
getMinVal(myarray)
