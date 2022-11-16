
___ gettheoddlyrepeatednumber(myarray
        print "myarray:",myarray
	i _ result _ 0
 	___ i __ range (0, l..(myarray)):
                #print result,"^",myarray[i],"is",result ^ myarray[i] 
		result _ result ^ myarray[i]
                 
	r_ result

myarray _ [70, 23, 16, 23, 23, 16, 70]
print gettheoddlyrepeatednumber(myarray)
