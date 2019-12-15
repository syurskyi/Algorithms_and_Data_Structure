from data import DICTIONARY, LETTER_SCORES


def load_words():
	"""
	:return: Loads in the dictionary (text file, with each word on a new line)
	"""
	with open(DICTIONARY, 'r') as file:
		# Read, remove whitespace, split each line as a word
		words = file.read().strip().split('\n')
	return words


def calc_word_value(word):
	"""
	:param word: A single word string containing only alphabet characters
	Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES
	"""
	# "For each letter in word, join it back together if the letter is an
	# alphabetical character"
	word = ''.join(letter for letter in word.upper() if letter.isalpha())

	# "Sum letter values for each letter in the word."
	score = sum(LETTER_SCORES.get(letter) for letter in list(word))
	return score


def max_word_value(dictionary=[]):
	"""
	:param dictionary: List of words. If none provided uses default DICTIONARY
	:return: Calculate the word with the max value in the dictionary.
	"""
	if dictionary == []: dictionary = load_words()

	# Find the maximum value in dictionary based on the key.
	# The key is the letter score of the word.
	best_word = max(dictionary, key=lambda word: calc_word_value(word))
	return best_word


if __name__ == "__main__":
	max_word_value()