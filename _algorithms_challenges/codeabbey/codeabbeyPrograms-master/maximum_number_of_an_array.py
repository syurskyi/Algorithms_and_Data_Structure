# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:27:24 2016

@author: rajan

Problem 15 // Maximum of numbers in an array


"""
print('Enter the numbers in an array separated by space ')
num_input = input()
num_array = num_input.split()
num_length = len(num_array)
max_num = float(num_array[0])
for i in range(1,num_length):
    if max_num < float(num_array[i]):
        max_num = float(num_array[i])
    i += 1
print('The maximum number of an array is ',max_num)
