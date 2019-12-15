print "This program is to check the prime number functionality"


def isPrime(n):
	
	if(n<=1):
		return False # prime should be greater than 1
	elif((n==2) or (n==3) or (n==5)):
		return True
	elif (n%3==0 or n%5==0):
		return False
	
	else:
		count=0
		for i in range (3,n/2+1,2):
			#print " ",i
			if n%i==0:
				count+=1
		#print count
		return count==0
	return False


def inputNumber():
	number = int(raw_input("Enter a number to check prime functionality > "))
	return number


result =  isPrime(inputNumber())

print result


