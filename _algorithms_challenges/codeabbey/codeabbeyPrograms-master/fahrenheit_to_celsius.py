# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 13:25:30 2016

@author: rajan

Problem 7

Conversion of Fahrenheit to Celsius

"""

print('Enter the values in fahrenheit you want to convert to celsius, separated by space')
fahrenheit_values = input().split()
result = []
c = 0
for x in fahrenheit_values:
    c = round((float(x) - 32.0)*5.0/9.0,2)
    result.append(c)
print('The converted array of celsius is ',result)
    
