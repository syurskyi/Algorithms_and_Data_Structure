# Write a method to decide if two strings are anagrams or not.

# "abc" "cba" => true
# "cinema" "iceman" => true
# "bumblebee" "icecream" => false

# O(nlogn)

def anagram(word1, word2):
	return sorted(word1) == sorted(word2)

# O(n) O(n)

def anagram2(word1, word2):
	if len(word1) != len(word2):
		return False

	dict1 = {}
	dict2 = {}

	for i in range(len(word1)):
		if word1[i] not in dict1.keys():
			dict1[word1[i]] = 1
		else:
			dict1[word1[i]] += 1

	for i in range(len(word2)):
		if word2[i] not in dict2.keys():
			dict2[word2[i]] = 1
		else:
			dict2[word2[i]] += 1

	for key, value in dict1.items():
		if dict2[key] != value:
			return False

	return True

print(anagram2("abc", "cba"))
print(anagram2("cinema", "iceman"))
print(anagram2("bumblebee", "icecream"))
print(anagram2("abc", "abc"))
