# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:02:36 2016

@author: rajan

Problem 9

To check whether a triangle can be drawn

"""

print('Enter the values for triangle sides in the form of triplets separated by space')
tri = input().split()
tri_array = []
l = len(tri)
i = 0

while i < l:
    triangle = []
    triangle = tri[i:i+3] 
    tri_array.append(triangle)
    i += 3
print(tri_array)
    
result = []
for ta in tri_array:
    r = 0
    ta.sort()
    a,b,c = int(ta[0]), int(ta[1]), int(ta[2])
    if a + b > c:
        r = 1
    result.append(r)
print('1 indicates the triangle can be drawn and 0 indicates triangle cant be drawn')
print('The result array is ',result)

