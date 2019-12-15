# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:40:05 2016

@author: rajan

Problem 6

This problem rounds off the number when divided by another number.
"""
print('Enter the numbers you want to divide. Dividend and divisor separated by space.')
num = input()
num_array = num.split()
l = len(num_array)
final_array = []
if l > 2:
    i = 0
    while i < l:
        splitted_array = []
        splitted_array = num_array[i:i+2]
        i += 2
        final_array.append(splitted_array)
else:
    final_array.append(num_array)
    
result_array = []
for x in final_array:
    result = 0
    result = round(float(x[0])/float(x[1]))
    result_array.append(result)
print('The resulting array is ',result_array )


