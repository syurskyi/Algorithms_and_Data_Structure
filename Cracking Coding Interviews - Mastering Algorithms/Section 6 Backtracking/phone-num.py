# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

mapping = {
	"2": "abc",
	"3": "def",
	"4": "ghi",
	"5": "jkl",
	"6": "mno",
	"7": "pqrs",
	"8": "tuv",
	"9": "wxyz",
}

def combos(digits):
	if len(digits) == 0:
		return []

	output = []

	cur_digit = digits[0]
	letters = mapping[cur_digit]

	remaining_combos = combos(digits[1:])

	for i in range(len(letters)):
		letter = letters[i]

		for word in remaining_combos:
			output.append(letter + word)

		if len(remaining_combos) == 0:
			output.append(letter)

	return output

print(combos("23"))
print(combos("2389"))
