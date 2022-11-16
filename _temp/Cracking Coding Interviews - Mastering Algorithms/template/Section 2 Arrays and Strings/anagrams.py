# Write a method to decide if two strings are anagrams or not.

# "abc" "cba" => true
# "cinema" "iceman" => true
# "bumblebee" "icecream" => false

# O(nlogn)

___ anagram(word1, word2
	r_ sorted(word1) == sorted(word2)

# O(n) O(n)

___ anagram2(word1, word2
	__ len(word1) !_ len(word2
		r_ False

	dict1 _ {}
	dict2 _ {}

	___ i __ range(len(word1)):
		__ word1[i] n.. __ dict1.keys(
			dict1[word1[i]] _ 1
		____
			dict1[word1[i]] +_ 1

	___ i __ range(len(word2)):
		__ word2[i] n.. __ dict2.keys(
			dict2[word2[i]] _ 1
		____
			dict2[word2[i]] +_ 1

	___ key, value __ dict1.items(
		__ dict2[key] !_ value:
			r_ False

	r_ True

print(anagram2("abc", "cba"))
print(anagram2("cinema", "iceman"))
print(anagram2("bumblebee", "icecream"))
print(anagram2("abc", "abc"))
