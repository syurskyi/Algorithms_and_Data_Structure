def praveen(a,b=1,c=2):
	print "\na = %s"%a
	print "b = %s"%b
	print "c = %s"%c

def praveen2(a=3,b=1,c=2):
        print "\na = %s"%a
        print "b = %s"%b
        print "c = %s"%c

def praveen3(a,b,c):
        print "\na = %s"%a
        print "b = %s"%b
        print "c = %s"%c


if __name__=="__main__":
	praveen(10)
	praveen(10,b=15)
	praveen(10,c=15)
	praveen2(a=2,b=3,c=1)
	praveen3(b=2,a=3,c=1)
