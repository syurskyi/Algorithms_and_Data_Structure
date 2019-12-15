# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:49:36 2016

@author: rajan gyawali

Problem 2

Sum of N numbers in loop

"""

print('Enter the number of numbers you want to sum')
n = int(input())
print('Enter the numbers you want to add separated by space')
nums = input()
num = nums.split()
sum = 0
for i in num:
    sum += float(i)
print('The sum  of numbers is ',sum)