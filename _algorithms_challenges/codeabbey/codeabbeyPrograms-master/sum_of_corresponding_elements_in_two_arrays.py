# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:02:21 2016

@author: rajan gyawali

problem 3

The program will find the sum of corresponding elements of two arrays

"""

print('Enter the length of the arrays')
l = int(input())
print('Enter the items for first array separated by space')
array1 = input().split()
print('Enter the items for second array separated by space')
array2 = input().split()
i = 0
result = []
while i < l:
    sum = 0
    sum = float(array1[i]) + float(array2[i])
    result.append(sum)
    i += 1
print('The result array is ',result)