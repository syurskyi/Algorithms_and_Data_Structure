# Write a method to decide if two strings are anagrams or not.

# "abc" "cba" => true
# "cinema" "iceman" => true
# "bumblebee" "icecream" => false

# O(nlogn)

def anagram(word1, word2):
	return sorted(word1) == sorted(word2)

# O(n) O(n)

___ anagram2 word1, word2
	__ l.. ? !_ l.. ?
		r_ F..

	dict1 _     # dict
	dict2 _     # dict

	___ i __ r..(l.. ?
		__ _1 ? n.. __ _1.k..
			_1 ? ? _ 1
		____
			_1 ? ? +_ 1

	___ i __ r.. l.. ?
		__ ? ? n.. __ _2.k..
			_2 ? ? _ 1
		____
			_2 ? ? +_ 1

	___ key, value __ _1.i..
		__ _2 ? !_ ?
			r_ F..

	r_ T..

print(anagram2("abc", "cba"))
print(anagram2("cinema", "iceman"))
print(anagram2("bumblebee", "icecream"))
print(anagram2("abc", "abc"))
