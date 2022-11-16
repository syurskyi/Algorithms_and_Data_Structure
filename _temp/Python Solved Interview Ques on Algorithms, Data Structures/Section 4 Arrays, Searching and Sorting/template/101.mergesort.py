
___ mymergesort(myarray
    #print "Array entering the function:",myarray
    __ l..(myarray) > 1:
        mid _ l..(myarray) // 2
        lefthalf _ myarray[:mid]
        righthalf _ myarray[mid:]
        #print "lefthalf:",lefthalf
        #print "righthalf:",righthalf
        mymergesort(lefthalf)
        mymergesort(righthalf)
        i _ j _ k _ 0
        _____ i < l..(lefthalf) and j < l..(righthalf
            #print "In first while loop myarray:",myarray
            __ lefthalf[i] < righthalf[j]:
                myarray[k] _ lefthalf[i]
                i _ i + 1
            ____
                myarray[k] _ righthalf[j]
                j _ j + 1
            k _ k + 1
        #print "while exiting first while loop:",myarray

        _____ i < l..(lefthalf
            #print "In second while loop myarray:",myarray
            myarray[k] _ lefthalf[i]
            i _ i + 1
            k _ k + 1
        #print "while exiting second while loop:",myarray

        _____ j < l..(righthalf
            #print "In third while loop myarray:",myarray
            myarray[k] _ righthalf[j]
            j _ j + 1
            k _ k + 1
        #print "while exiting third while loop:",myarray

myarray_[600,500,400,300,200,100]
print "given array:",myarray
mymergesort(myarray)
print(myarray)
