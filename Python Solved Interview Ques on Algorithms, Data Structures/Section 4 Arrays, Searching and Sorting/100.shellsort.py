
def myShellSort(myarray):
    print "input myarray:", myarray
    sublistcount = len(myarray) // 2
    while sublistcount > 0:
        #print "sublistcount in myshellsort function:",sublistcount
        for spos in range(sublistcount):
            #print "in myshellsort function:",spos
            myinsertionsort(myarray, spos, sublistcount)

        sublistcount = sublistcount // 2
        #print "PRINTING myarray in outer myShellSort function:",myarray

def myinsertionsort(myarray, s, g):
    #print "In myinsertionsort function:","myarray:",myarray,"s:",s,"g:",g
    #for j in range(s + g, len(myarray), g):
        #print "array for range(s:",s,"+ g:",g,"len(myarray):",len(myarray),"g:",g,") is:", myarray[j]
    for i in range(s + g, len(myarray), g):
        cv = myarray[i]
        pos = i
        #print "in outer loop:",myarray
        #print "cv:",cv
        #print "pos:",i
        while pos >= g and myarray[pos - g] > cv:
            #print "in while loop where pos >=g and myarray[pos - g] > cv:",pos,">=",g,"and myarray[",pos - g,"] >",cv
            #print "copying myarray[",pos-g,"] to myarray [",pos,"]"
            myarray[pos] = myarray[pos - g]
            pos = pos - g
            #print "in inner loop:",myarray
            #print "changed pos from ",pos + g,"to",pos

        #print "once you are out of while loop: myarray[",pos,"] contains",cv
        myarray[pos] = cv
    #print "output from Insertion sort:",myarray    
    #print "value of i:",i 

myarray=[400,300,200,100]
myShellSort(myarray)
print(myarray)
