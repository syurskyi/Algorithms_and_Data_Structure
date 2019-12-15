# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:49:15 2016

@author: rajan gyawali

Problem 11

Problem statement

Input data are in the following format:

    first line contains N - the number of values to process;
    and then N lines will follow describing the values for which sum of digits should be calculated by 3 integers A B C;
    for each case you need to multiply A by B and add C (i.e. A * B + C) - then calculate sum of digits of the result.

"""

print('How many test cases do you want ?')
n = int(input())
print('Enter the test cases in the form of A, B and C separated by space')

input_list = []
for i in range(1,n+1):
    lst = []
    print('Enter the values for the test  case {}'.format(i))
    lst = input().split()
    input_list.append(lst)
    
def split(n):
    split_list = []
    num = int(n)
    while num != 0:
        r = num % 10
        q = num//10
        num = q
        split_list.append(r)
    s = 0
    for i in range(0,len(split_list)):
        s += int(split_list[i])
    print('The sum of digits is ',s)
        

result_list = []   
for il in input_list:
    s = 0
    r = 0
    temp = []
    a, b, c = int(il[0]), int(il[1]), int(il[2])
    r = a*b + c
    temp = split(r)

        
        
        
    