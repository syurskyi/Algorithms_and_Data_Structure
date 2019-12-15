# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:26:48 2016

@author: rajan

Problem 10

Linear function in the form of y = ax + b

we have to find the values of (a,b) for the given two pairs of (x,y)

"""

print('How many test cases do you want ?')
n = int(input())
input_list = []
for i in range(1,n+1):
    print('Enter the two pairs of (x,y) each separated by space for the Test Case {}'.format(i))
    lst = input().split()
    l = len(lst)
    lis = []
    for k in range(0,l):
        lt = []
        lt = lst[k]
        lis.append(lt)
    input_list.append(lis)
    i += 1
print('---------------------')
print(input_list)
print('---------------------')
output_list = []
for il in input_list:
    ol = []
    a,b = 0,0
    x1,y1,x2,y2 = int(il[0]), int(il[1]), int(il[2]), int(il[3])
    a = (y2 - y1)/(x2 - x1)
    ol.append(a)
    b = y1 - a*x1
    ol.append(b)
    output_list.append(ol)
print('The output list for (a,b) is ',output_list)
    