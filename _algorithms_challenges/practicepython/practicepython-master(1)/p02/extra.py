entry = int(input("enter a number: "))

if entry % 2 == 0:
	print("this is even")

else:
	print("this is odd")

if entry % 4 == 0:
	print("this is a multiple of 4")

num = int(input("enter a number to check: "))
check = int(input("enter a number to divide by: "))

if num % check == 0:
	print("this divides evenly")

else:
	print("this does not divide evenly")