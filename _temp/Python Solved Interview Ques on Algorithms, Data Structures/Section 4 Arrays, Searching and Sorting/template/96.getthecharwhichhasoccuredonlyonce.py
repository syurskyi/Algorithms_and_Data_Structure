
___ getelemwhichhassingleoccurence(myarray
        print "Given array:", myarray
	hashTable _ {}
	___ elem __ myarray.lower(
		__ elem __ hashTable:
			hashTable[elem] +_ 1
		elif elem !_ " ":
			hashTable[elem] _ 1
		____
			hashTable[elem] _ 0
                #print ">> start loop: Array:",myarray
                #print "               hashTable:", hashTable
                #print "<<end loop"


	___ elem __ myarray.lower(
		__ hashTable[elem] __ 1:
                        print "the first non repeated  character is:" ,elem
			r_ elem

	r_
 
getelemwhichhassingleoccurence("aabcc")
