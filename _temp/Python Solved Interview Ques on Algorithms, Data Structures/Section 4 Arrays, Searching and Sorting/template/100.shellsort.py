
___ myShellSort(myarray
    print "input myarray:", myarray
    sublistcount _ l..(myarray) // 2
    _____ sublistcount > 0:
        #print "sublistcount in myshellsort function:",sublistcount
        ___ spos __ r..(sublistcount
            #print "in myshellsort function:",spos
            myinsertionsort(myarray, spos, sublistcount)

        sublistcount _ sublistcount // 2
        #print "PRINTING myarray in outer myShellSort function:",myarray

___ myinsertionsort(myarray, s, g
    #print "In myinsertionsort function:","myarray:",myarray,"s:",s,"g:",g
    #for j in range(s + g, len(myarray), g):
        #print "array for range(s:",s,"+ g:",g,"len(myarray):",len(myarray),"g:",g,") is:", myarray[j]
    ___ i __ r..(s + g, l..(myarray), g
        cv _ myarray[i]
        pos _ i
        #print "in outer loop:",myarray
        #print "cv:",cv
        #print "pos:",i
        _____ pos >_ g ___ myarray[pos - g] > cv:
            #print "in while loop where pos >=g and myarray[pos - g] > cv:",pos,">=",g,"and myarray[",pos - g,"] >",cv
            #print "copying myarray[",pos-g,"] to myarray [",pos,"]"
            myarray[pos] _ myarray[pos - g]
            pos _ pos - g
            #print "in inner loop:",myarray
            #print "changed pos from ",pos + g,"to",pos

        #print "once you are out of while loop: myarray[",pos,"] contains",cv
        myarray[pos] _ cv
    #print "output from Insertion sort:",myarray    
    #print "value of i:",i 

myarray_[400,300,200,100]
myShellSort(myarray)
print(myarray)
