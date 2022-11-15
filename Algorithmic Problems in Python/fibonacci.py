
def fibonacci(n):

	#we have to define the base cases
	#F(0)=1 and F(1)=1
	if n==0: return 0
	if n==1: return 1

	#head 001_recursion: first we call the function recursively
	#overlapping subproblems so better approach would be to use dynamic programming
	fib1 = fibonacci(n-1)
	fib2 = fibonacci(n-2)
	
	#do some operation after 001_recursion
	result = fib1+fib2
	
	return result

	
if __name__ == "__main__":

	print(fibonacci(10))