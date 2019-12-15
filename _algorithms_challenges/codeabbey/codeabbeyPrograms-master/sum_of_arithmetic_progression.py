# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:40:25 2016

@author: rajan

Problem 8

This calculates the sum of numbers in arithmetic progression

"""

print('How many Arithmetic progressions sum do you want')
n = int(input())
print('Enter the data in the form of triplets: A = Starting Value, B = Step Size, C = number of values')
input_triplets = []
for i in range(0,n):
    input_triplet = []
    print('Enter the values of A, B and C for triplet  {} separated by space.'.format(i))
    input_triplet = input().split()
    input_triplets.append(input_triplet)
    i += 1
print(input_triplets)
    
result = []
for it in input_triplets:
    res = 0
    a = int(it[0])
    n = int(it[2])
    d = int(it[1])
    res = (n/2)*(2*a + (n - 1)*d)
    result.append(res)
print('The result array is ',result)
    
