# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.


# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from string import ascii_lowercase
import copy

class Node:
	def __init__(self, word, path):
		self.word = word
		self.path = path

def ladder(begin, end, word_list):
	queue = []

	words = set(word_list)

	queue.append(Node(begin, [begin]))

	while len(queue) > 0:
		cur = queue.pop(0)

		cur_word = cur.word
		path = cur.path

		if cur_word == end:
			return path

		for i in range(len(cur_word)):
			for c in ascii_lowercase:
				potential_word = cur_word[:i] + c + cur_word[i+1:]

				if potential_word in words:
					copy_path = copy.deepcopy(path)
					copy_path.append(potential_word)
					queue.append(Node(potential_word, copy_path))
					words.remove(potential_word)

	return []

print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))













