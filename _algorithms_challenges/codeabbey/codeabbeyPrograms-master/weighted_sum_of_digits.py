# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:05:10 2016

@author: rajan gyawali

Problem #13 

Weighted sum of digits

This program resembles more complex algorithms for calculation CRC 
and other checksums and also hash-functions on character strings.

wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60


"""
print('Enter the numbers you want to find weighted sum separated by space.')
num = input().split()
result = []

def sod(n):
    split_list = []
    num = int(n)
    while num != 0:
        r = num % 10
        q = num//10
        num = q
        split_list.append(r)
    split_list.reverse()
    sum = 0   
    for i in range(0,len(split_list)):
        sum += split_list[i]*(i+1)
    return sum

for n in num:
    y = sod(n)
    result.append(y)
print('The result array of weighted sum is ',result)
