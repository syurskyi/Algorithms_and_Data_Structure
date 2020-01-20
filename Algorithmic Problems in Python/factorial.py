
def factorial(n):

	#base case: 1!=1 (factorial 1 is 1)
	if n == 1:
		return 1
        
	#we make a recursive call
	subres1 = factorial(n-1)	
	
	#we do some operations
	subres2 = n*subres1		
	
	return subres2	
	
def factorial_accumulator(n,accumulator=1):

	#base case: 1!=1
	if n==1:
		return accumulator
		
	#now it is a tail recursion !!!
	return factorial_accumulator(n-1,n*accumulator)
	
if __name__ == "__main__":

	print(factorial_accumulator(5))