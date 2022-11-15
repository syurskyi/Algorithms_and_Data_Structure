# ((()())()) => True
# )())) = False
# (() => False
# )( => False

def check(s):
    left = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    return left == 0

print(check("((()())())"))
print(check("(()()))"))
print(check(")("))