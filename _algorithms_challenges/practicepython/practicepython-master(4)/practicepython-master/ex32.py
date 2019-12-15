import ex31
import ex30


#ex30 is used to pick a word from a file
#ex31 is used to check guesses for win in hangman game


if __name__=="__main__":
	word = ex30.pick_word()
	#print word
	ex31.guess_letter(word)
	print word
