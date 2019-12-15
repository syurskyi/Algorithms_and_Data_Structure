name = raw_input("Enter your name> ")
age = int(raw_input("Enter your age> "))



str = "Hi %s your will become 100 years old in %d years \n\n" % (name,2017+(100-age))
print str

no_of_times = int(raw_input("How many times do you want to print the above msg ? > "))

print str * no_of_times

