___ dflag(myarray
    print "given array:",myarray
    n _ l..(myarray)
    zeroIndex _ 0; twoIndex _ n - 1
    currentIndex _ 0
    _____ currentIndex <_ twoIndex:
        ##print "CURIndex:",currentIndex,"MYARRAY:",myarray,"ZEROIndex:",zeroIndex,"TWOIndex:",twoIndex
        __ myarray[currentIndex] __ 0:
            __ currentIndex > zeroIndex:
                #print "currentIndex:",currentIndex,"is > then zeroIndex:",zeroIndex
                #print "myarray[currentIndex:",currentIndex,"] is 0, so exchanging myarray[",zeroIndex,"] and myarray[",currentIndex,"]:",myarray[zeroIndex], "with", myarray[currentIndex]
                myarray[zeroIndex], myarray[currentIndex] _ myarray[currentIndex], myarray[zeroIndex]
                #print "moving zeroindex from",zeroIndex,"to",zeroIndex+1
                zeroIndex +_ 1
            ____
                currentIndex +_ 1
                zeroIndex +_ 1
        
        ____ myarray[currentIndex] __ 2:
            __ currentIndex < twoIndex:
                #print "currentIndex:",currentIndex,"is < then twoIndex:",twoIndex
                #print "myarray[currentIndex:",currentIndex,"] is 2, so exchanging myarray[",twoIndex,"] and myarray[",currentIndex,"]:",myarray[twoIndex], "with", myarray[currentIndex]
                myarray[twoIndex], myarray[currentIndex] _ myarray[currentIndex], myarray[twoIndex]
                #print "moving twoIndex from",twoIndex,"to",twoIndex-1
                twoIndex -_ 1
            ____
                b..
        ____
            currentIndex +_ 1
    print myarray, '\n'
    r_ myarray

__ __name__ __ '__main__':
#     dflag([0,1,2])   
#      dflag([0,2,1])   
#      dflag([2, 0, 1, 0, 2])
     dflag([2, 0, 1, 0, 2, 1, 2, 2, 1, 1])
#    dutchflag([2, 1, 2, 1, 2, 0])
#    dutchflag([0, 0, 1, 2, 2, 2, 0, 0, 0])
