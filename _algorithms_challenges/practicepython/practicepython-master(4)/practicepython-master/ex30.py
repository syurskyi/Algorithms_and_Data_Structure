# read a random word from the sowpods dictionary file

import random

def pick_word():
	with open("sowpods.txt") as sowpod_file:
		word = sowpod_file.readline().strip()
		wordlist = []
	
		while word:
			wordlist.append(word)
			word = sowpod_file.readline().strip()
		#print len(wordlist)
		random_word_index = random.randint(0,len(wordlist)-1)
		#print wordlist[random_word_index]
		return wordlist[random_word_index]


if __name__=="__main__":
	print	pick_word()
