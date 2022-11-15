# Given a string containing just the characters
# '(', ')',
# '{', '}',
# '[' and ']',
# determine if the input string is valid

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

# Example 4:
# Input: "([)]"
# Output: false

# Example 5:
# Input: "{[]}"
# Output: true

def balanced(s):
	stack = []

	for i in range(len(s)):
		if s[i] == "(" or s[i] == "{" or s[i] == "[":
			stack.append(s[i])
		elif s[i] == ")" and (len(stack) == 0 or stack.pop() != "("):
			return False
		elif s[i] == "]" and (len(stack) == 0 or stack.pop() != "["):
			return False
		elif s[i] == "}" and (len(stack) == 0 or stack.pop() != "{"):
			return False

	return len(stack) == 0



print(balanced("()"))
print(balanced("()[]{}"))
print(balanced("(]"))
print(balanced("([)]"))
print(balanced("{[]}"))
