
def getelemwhichhassingleoccurence(myarray):
        print "Given array:", myarray
	hashTable = {}  
	for elem in myarray.lower():
		if elem in hashTable:
			hashTable[elem] += 1
		elif elem != " ":
			hashTable[elem] = 1
		else:
			hashTable[elem] = 0
                #print ">> start loop: Array:",myarray
                #print "               hashTable:", hashTable
                #print "<<end loop"


	for elem in myarray.lower():
		if hashTable[elem] == 1:
                        print "the first non repeated  character is:" ,elem
			return elem

	return
 
getelemwhichhassingleoccurence("aabcc")
