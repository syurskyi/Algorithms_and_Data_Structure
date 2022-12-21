# Implement an algorithm to determine if a string has all unique characters.

# "abc" -> True
# "" -> True
# "aabc" -> False

# Brute Force - O(n^2)
# Sorting - O(nlogn + n) -> O(nlogn)
# Hashset - O(n)

def unique_characters(word):
	visited_chars = set()

	for i in range(len(word)):
		letter = word[i]

		if letter in visited_chars:
			return False

		visited_chars.add(letter)

	return True

print(unique_characters("abc"))
print(unique_characters(""))
print(unique_characters("aabc"))
