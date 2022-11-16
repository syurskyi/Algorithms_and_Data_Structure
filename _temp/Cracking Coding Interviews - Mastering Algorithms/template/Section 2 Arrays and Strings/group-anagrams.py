# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# O(n * mlogm)

___ group_anagrams(strs
	dic _     # dict

	___ i __ r..(l..(strs
		sorted_anagram _ "".join(s..(strs[i]))
		group_strs _ dic.get(sorted_anagram,    # list)
		group_strs.a..(strs[i])

		dic[sorted_anagram] _ group_strs

	r_ list(dic.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# O(n*m)
# Prime factorizations for each letter
