# Implement an algorithm to determine if a string has all unique characters.

# "abc" -> True
# "" -> True
# "aabc" -> False

# Brute Force - O(n^2)
# Sorting - O(nlogn + n) -> O(nlogn)
# Hashset - O(n)

___ unique_characters(word
	visited_chars _ set()

	___ i __ r..(l..(word
		letter _ word[i]

		__ letter __ visited_chars:
			r_ F..

		visited_chars.add(letter)

	r_ T..

print(unique_characters("abc"))
print(unique_characters(""))
print(unique_characters("aabc"))
