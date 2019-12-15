number = int(input("enter a number "))

complete = list(range(2, number+1))

divisors = []

for ele in complete:
	if number % ele == 0:
		divisors.append(ele)

print(divisors)