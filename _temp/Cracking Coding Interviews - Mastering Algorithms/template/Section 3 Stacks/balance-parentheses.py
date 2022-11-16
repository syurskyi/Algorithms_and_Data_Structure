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

___ balanced(s
	stack _    # list

	___ i __ range(l..(s)):
		__ s[i] __ "(" or s[i] __ "{" or s[i] __ "[":
			stack.a..(s[i])
		elif s[i] __ ")" and (l..(stack) __ 0 or stack.pop() !_ "("
			r_ False
		elif s[i] __ "]" and (l..(stack) __ 0 or stack.pop() !_ "["
			r_ False
		elif s[i] __ "}" and (l..(stack) __ 0 or stack.pop() !_ "{"
			r_ False

	r_ l..(stack) __ 0



print(balanced("()"))
print(balanced("()[]{}"))
print(balanced("(]"))
print(balanced("([)]"))
print(balanced("{[]}"))
