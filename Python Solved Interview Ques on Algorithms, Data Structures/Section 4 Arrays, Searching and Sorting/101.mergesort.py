
def mymergesort(myarray):
    #print "Array entering the function:",myarray
    if len(myarray) > 1:
        mid = len(myarray) // 2
        lefthalf = myarray[:mid]
        righthalf = myarray[mid:]
        #print "lefthalf:",lefthalf
        #print "righthalf:",righthalf
        mymergesort(lefthalf)
        mymergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            #print "In first while loop myarray:",myarray
            if lefthalf[i] < righthalf[j]:
                myarray[k] = lefthalf[i]
                i = i + 1
            else:
                myarray[k] = righthalf[j]
                j = j + 1
            k = k + 1
        #print "while exiting first while loop:",myarray

        while i < len(lefthalf):
            #print "In second while loop myarray:",myarray
            myarray[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        #print "while exiting second while loop:",myarray

        while j < len(righthalf):
            #print "In third while loop myarray:",myarray
            myarray[k] = righthalf[j]
            j = j + 1
            k = k + 1
        #print "while exiting third while loop:",myarray

myarray=[600,500,400,300,200,100]
print "given array:",myarray
mymergesort(myarray)
print(myarray)
