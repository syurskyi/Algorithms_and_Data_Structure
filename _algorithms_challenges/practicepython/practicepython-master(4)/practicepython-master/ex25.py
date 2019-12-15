#guess the random number game part two 
#keep a number between 0 and 100 ask the system to guess a random number between 0 and 100 and tell how many
#times has guessed it correctly


import random


user_number = raw_input("type  the number in your mind. dont worry we will use for verification only> ")
def guess(low,high,try_count,user_input=None):
	system_guess = random.randint(low,high)
	#try_count = 0

	while user_input!="exit":
		#print "Random number is %d , your guess is %d " %(system_number,user_input)
		try_count +=1
		print "system_guess"
		print system_guess
		print "Is the above number correct. provide input (high,low or equal) for system to guess again"
		user_input = raw_input("Enter high/low/equal> ")

		if(user_input == "equal"):
			print "Yeah I guessed it right in %d chances. Cheers."%(try_count)
			return
		elif( user_input == "low"):
			print "going to guess high"
			guess(system_guess,high,try_count)
			return
			
		else:
			print "going to guess little low"
			guess(low,system_guess,try_count)
			return
	
		user_input = raw_input("Guess again or type exit> ")

		print "Bye..."

guess(0,10,0)
