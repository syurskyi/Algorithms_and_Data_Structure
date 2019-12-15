#program to get input n from user and generate n fibonaucci numbers 


def get_input(msg="Enter an integer"):
	return int(raw_input(msg))


def fibonaucci(n):
	count = 0
	a = 0
	b = 1
	while count<=n:
		c = a+b
		a = b
		b = c
		print a,
		count +=1

def printfib():
	number = get_input("Enter a number n")
	fibonaucci(number)


if __name__ == "__main__":
	printfib()



