"""
Write a Python program to check whether a specified value is contained in a group of values.
"""

def is_included(list,n):
    return n in list

print(is_included([0,3,2],3))
print(is_included([0,2,3,1],5))