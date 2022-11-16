# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

mapping _ {
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz",
}

___ combos(digits
	__ len(digits) == 0:
		r_ []

	output _ []

	cur_digit _ digits[0]
	letters _ mapping[cur_digit]

	remaining_combos _ combos(digits[1:])

	___ i __ range(len(letters)):
		letter _ letters[i]

		___ word __ remaining_combos:
			output.append(letter + word)

		__ len(remaining_combos) == 0:
			output.append(letter)

	r_ output

print(combos("23"))
print(combos("2389"))
