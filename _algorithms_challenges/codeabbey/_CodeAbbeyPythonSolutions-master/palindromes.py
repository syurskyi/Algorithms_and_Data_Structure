import re

amount_values = int(input())
results = []

def is_palindrome(string):
    string = string.replace(" ", "")
    string = re.sub(r'[^\w\s]','',string).lower()
    string_length = len(string)
    for i in range(string_length//2):
        if(string[i] != string[string_length-i-1]):
            return "N"
    return "Y"

for i in range(amount_values):
    string = input()
    results.append(is_palindrome(string))

print(*results)