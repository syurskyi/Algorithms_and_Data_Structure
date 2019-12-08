def dflag(myarray):
    print "given array:",myarray
    n = len(myarray)
    zeroIndex = 0; twoIndex = n - 1
    currentIndex = 0
    while currentIndex <= twoIndex:
        ##print "CURIndex:",currentIndex,"MYARRAY:",myarray,"ZEROIndex:",zeroIndex,"TWOIndex:",twoIndex
        if myarray[currentIndex] == 0:
            if currentIndex > zeroIndex:
                #print "currentIndex:",currentIndex,"is > then zeroIndex:",zeroIndex
                #print "myarray[currentIndex:",currentIndex,"] is 0, so exchanging myarray[",zeroIndex,"] and myarray[",currentIndex,"]:",myarray[zeroIndex], "with", myarray[currentIndex]
                myarray[zeroIndex], myarray[currentIndex] = myarray[currentIndex], myarray[zeroIndex]
                #print "moving zeroindex from",zeroIndex,"to",zeroIndex+1
                zeroIndex += 1
            else: 
                currentIndex += 1
                zeroIndex += 1
        
        elif myarray[currentIndex] == 2:
            if currentIndex < twoIndex:
                #print "currentIndex:",currentIndex,"is < then twoIndex:",twoIndex
                #print "myarray[currentIndex:",currentIndex,"] is 2, so exchanging myarray[",twoIndex,"] and myarray[",currentIndex,"]:",myarray[twoIndex], "with", myarray[currentIndex]
                myarray[twoIndex], myarray[currentIndex] = myarray[currentIndex], myarray[twoIndex]
                #print "moving twoIndex from",twoIndex,"to",twoIndex-1
                twoIndex -= 1
            else:
                break
        else:
            currentIndex += 1
    print myarray, '\n'
    return myarray

if __name__ == '__main__':
#     dflag([0,1,2])   
#      dflag([0,2,1])   
#      dflag([2, 0, 1, 0, 2])
     dflag([2, 0, 1, 0, 2, 1, 2, 2, 1, 1])
#    dutchflag([2, 1, 2, 1, 2, 0])
#    dutchflag([0, 0, 1, 2, 2, 2, 0, 0, 0])
