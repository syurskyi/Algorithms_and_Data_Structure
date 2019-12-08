
def getthefrequencyofeverynumber(myarray):
        print "Given array:",myarray
	hashTable = {}  
        #print "created hash:",hashTable
	for ele in myarray:
		if ele in hashTable:
			hashTable[ele] += 1
		elif ele != " ":
			hashTable[ele] = 1
		else:
			hashTable[ele] = 0
                #print ">> start loop: Array:",myarray
                #print "               hashTable:", hashTable
                #print "<<end loop"

	for ele in myarray:
		print ele, "frequency", hashTable[ele]
 
myarray = [100, 25, 25, 120, 100] 
getthefrequencyofeverynumber(myarray)
