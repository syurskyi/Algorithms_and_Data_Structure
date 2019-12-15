# tic tac go game grid drawing

def draw(n):
	vblock = "|    " * (n+1)
	hblock = " --- " * n

	for i in range(0,n):
		print hblock
		print vblock
	print hblock



n  = int(raw_input("Enter the number of boxes to draw > "))

draw(n)
