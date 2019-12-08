
def gettheoddlyrepeatednumber(myarray):
        print "myarray:",myarray
	i = result = 0
 	for i in range (0, len(myarray)):
                #print result,"^",myarray[i],"is",result ^ myarray[i] 
		result = result ^ myarray[i]
                 
	return result

myarray = [70, 23, 16, 23, 23, 16, 70]
print gettheoddlyrepeatednumber(myarray)
