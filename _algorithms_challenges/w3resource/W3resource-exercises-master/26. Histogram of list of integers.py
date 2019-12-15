"""
Write a Python program to create a histogram from a given list of integers.
"""

def makehistogram(list):
    for n in list:
        print("*" * n)

print(makehistogram([1,4,5,9,3,2,3]))
