
#tail recursion
def tail(n):

	#base case
	if n==0:
		return
		
	#do some operation before the recursive call
	print(n)
	
	#recursive call
	tail(n-1)

def head(n):

	#base case 
	if n==0:
		return
	
	#recursive call
	head(n-1)
	
	#do some operation after the recursive call
	print(n)
	
if __name__ == "__main__":

	print("Tail recursion:\n")
	tail(5)
	print("\nHead recursion:\n")
	head(5)