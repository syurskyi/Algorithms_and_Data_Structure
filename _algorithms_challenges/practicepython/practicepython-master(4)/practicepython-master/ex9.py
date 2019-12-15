#guess the random number game
#ask the user to guess a random number between 1 and 9 and tell how many
#times he has guessed it corretly


import random


user_input = raw_input("guess a the number between 1 and 9> ")

system_number = random.randint(1,9)
try_count = 0

while user_input!="exit":
	#print "Random number is %d , your guess is %d " %(system_number,user_input)
	try_count +=1
	user_input = int(user_input)
	if(user_input == system_number):
		print "You guessed it right in %d chances. Cheers."%(try_count)
		break
	elif( user_input < system_number):
		print "You guessed a little low"
	else:
		print "You guessed a little high"
	
	user_input = raw_input("Guess again or type exit> ")


print "Bye..."
