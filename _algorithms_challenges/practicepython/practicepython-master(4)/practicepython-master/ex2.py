#odd or even

def even(number):
	if(number%4 == 0):
		print "Number is a multiple of 4 so different message printed"
		return
	elif number % 2 ==0:
		print "You entered an even number"
	else:
		print "You entered an odd number"



number = int(raw_input("Enter a number to check if its even> "))
divnum = int(raw_input("Enter another number to check whether above num can be divide evenly"))
even(number)


if(number%divnum == 0):
	print "new number Divides the above number evenly"
else:
	print "new number Does not divide the above number evenly"

