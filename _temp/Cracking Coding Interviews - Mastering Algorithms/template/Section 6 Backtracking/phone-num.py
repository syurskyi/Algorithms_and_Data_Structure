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
	__ l..(digits) __ 0:
		r_    # list

	output _    # list

	cur_digit _ digits[0]
	letters _ mapping[cur_digit]

	remaining_combos _ combos(digits[1:])

	___ i __ range(l..(letters)):
		letter _ letters[i]

		___ word __ remaining_combos:
			output.a..(letter + word)

		__ l..(remaining_combos) __ 0:
			output.a..(letter)

	r_ output

print(combos("23"))
print(combos("2389"))
