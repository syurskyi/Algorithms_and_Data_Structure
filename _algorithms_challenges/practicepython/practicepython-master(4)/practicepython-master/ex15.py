#reverse word order
#enter a sentence and print the words in reverse order


def get_input(inputmsg="Enter  a String > "):
	return raw_input(inputmsg)


def reverse_sentence(sentence):
	reversed_sentence = sentence.split()
	
	return " ".join(reversed_sentence[::-1])

if __name__ == "__main__":

	userinput = get_input()

	print reverse_sentence(userinput)
