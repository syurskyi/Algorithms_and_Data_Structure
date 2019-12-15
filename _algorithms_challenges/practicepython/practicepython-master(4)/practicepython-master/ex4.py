# get an input from an user an print all the divisors for that number



number = int(raw_input("Enter a number to print all its divisors> "))


newlist = [i for i in range(1,number+1) if number % i == 0]

print newlist	
