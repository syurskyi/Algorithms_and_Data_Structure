"""
Write a Python program to get the n (non-negative integer)
copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2
"""

def returncopies(str,n):
    if len(str) > 2:
        return str[:2] * n
    return str*n
print(returncopies("mi",11))
print(returncopies("chocolate",3))
