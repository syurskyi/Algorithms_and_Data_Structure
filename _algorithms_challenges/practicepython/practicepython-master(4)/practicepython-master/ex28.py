#max of three numbers


def get_input(msg="Input an integer > "):
	return int(raw_input(msg))




a = get_input()
b= get_input()
c= get_input()


print "maximum number is "
if((a > b) and (a > c)):
	print a
elif ((b > a) and (b > c)):
	print b
else:
	print c

