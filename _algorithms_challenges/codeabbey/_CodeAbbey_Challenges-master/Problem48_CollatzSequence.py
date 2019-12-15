with open("prob48.txt") as infile:
    infile.readline()
    data = infile.readline().strip().split(" ")

##    for start in data:
##        start = int(start)
##        count = 0
##        while start != 1:
##            count+=1
##            if int(start)%2 == 0: ## it is even
##                start = start/2
##            else:
##                start = (start*3)+1
##        print(count, end=" ")
            
# ALT


##def Collatz(start):  # int
##    global count
##    count+=1
##    if start == 1:
##        count-=1
##        return count
##    elif start%2 == 0:# EVEN
##        return Collatz(start/2)
##    else:
##
##        return Collatz((start*3)+1)
##
##for start in data:
##    count = 0  ## have to reset everytime 
##    start = int(start)
##    print(Collatz(start),end=" ")

