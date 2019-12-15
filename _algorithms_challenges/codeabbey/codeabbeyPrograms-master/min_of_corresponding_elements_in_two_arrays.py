# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:02:21 2016

@author: rajan gyawali

problem 4

The program will find the minimum of corresponding elements of two arrays

"""

print('Enter the length of the arrays')
l = int(input())
print('Enter the items for first array separated by space')
array1 = input().split()
print('Enter the items for second array separated by space')
array2 = input().split()
i = 0
min = []
while i < l:
    s = 0
    if float(array1[i]) < float(array2[i]):
        s = float(array1[i]) 
    else:
        s = float(array2[i])
    min.append(s)
    i += 1
print('The minimum values array is ',min)