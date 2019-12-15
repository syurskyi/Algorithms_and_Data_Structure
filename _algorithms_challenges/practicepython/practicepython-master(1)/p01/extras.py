name = input("what is your name? ")
age = int(input("what is your age? "))

currrent_year = 2016

centennial = (currrent_year - age) + 100

message = name + ", you will be 100 in the year " + str(centennial) + "\n"

print(message)

numberOfTimes = int(input("enter a number "))

print(message * numberOfTimes)