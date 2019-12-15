#guess letter module


def guess_letter(word):
	print "Welcome to hangman!"
	
	guess_word = "_"*len(word)
	guesslist = [letter for letter in guess_word]

	print guesslist
	guess_count =0
	count = len(word)
	incorrect_guess = 0
	while  incorrect_guess < 6 and count>0:
		guess_left = 6 - incorrect_guess
		#print '*'*10
		print "\nYou have %d incorrect guesses left"%guess_left
		letter = raw_input("\nGuess your letter: > ")
		guess_count += 1
		if letter in word:
			print "correct"
			for i in range(0,len(word)):
				if word[i] == letter:
					if guesslist[i]=='_':
						guesslist[i]=letter
						count-=1
					else:
						#incorrect_guess +=1
						print "You already guessed this"
			
		else:
			print "incorrect"
			incorrect_guess +=1
		print guesslist
		#print '*'*10
	if('_' in guesslist):
		print "You lost buddy"
	else:
		print "Cheers you have made it in %d guesses "%guess_count
	return guess_count
if __name__ == "__main__":
	guess_letter("EVAPORATE")
