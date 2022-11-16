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

c_ Node:
	___ -  word, path
		word _ word
		path _ path

___ ladder(begin, end, word_list
	queue _    # list

	words _ set(word_list)

	queue.a..(Node(begin, [begin]))

	_____ l..(queue) > 0:
		cur _ queue.p.. 0)

		cur_word _ cur.word
		path _ cur.path

		__ cur_word __ end:
			r_ path

		___ i __ r..(l..(cur_word
			___ c __ ascii_lowercase:
				potential_word _ cur_word[:i] + c + cur_word[i+1:]

				__ potential_word __ words:
					copy_path _ copy.deepcopy(path)
					copy_path.a..(potential_word)
					queue.a..(Node(potential_word, copy_path))
					words.remove(potential_word)

	r_    # list

print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))













