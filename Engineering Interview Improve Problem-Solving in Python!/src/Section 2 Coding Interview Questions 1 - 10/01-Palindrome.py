#Palindrome abc -> cba
#           aba -> aba

def reverse_string(s):
    result = ""
    for c in s:
        result = c + result
    return result

def is_palindrome(s):
    return s == reverse_string(s)


print(is_palindrome("abc"))
print(is_palindrome("aba"))
