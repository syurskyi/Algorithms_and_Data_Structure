##import math
##infile = open("prob22.txt")
##infile.readline()
##data = infile.readlines()
##infile.close()
##
##for line in data:
##    x,y,n = line.strip().split(" ")
##    if int(x)>int(y): # make X to be the smaller ones
##        x,y=y,x
##    x= int(x)
##    y= int(y)
##    n = int(n)
##    page_x = n//2  #round down
##    page_y = math.ceil(n/2) # round up
##    while page_x*x < page_y*y:
####        print(page_x,page_y)
##        if page_x*x == page_y*y:
##            break
##        page_x +=1
##        page_y -=1
##        if page_x*x > (page_y+1)*y:
##            page_x -=1
##            page_y +=1
##            break
####    print(page_x,page_y)
##    if page_x*x > page_y*y :
##        print(page_x*x,end=" ")
##    else:
##        print(page_y*y,end=" ")
result=[]
secondsA, secondsB, pages = [3,7,6]
# convert seconds/page to pages/second
rateA = 1/secondsA
rateB = 1/secondsB
# minimum time required to print at combined rate
totalTime = pages/(rateA + rateB)
# see how much extra time (if any) is needed to get the final page
extraTimeA = secondsA - (totalTime % secondsA)
extraTimeB = secondsB - (totalTime % secondsB)
# add the shortest time required for final page
totalTime += min(extraTimeA,extraTimeB)
result.append(int(totalTime))
