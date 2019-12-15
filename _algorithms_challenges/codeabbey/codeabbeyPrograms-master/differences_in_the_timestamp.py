# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 07:17:39 2016

@author: rajan gyawali



Problem #12 

Modulo and time difference

This program will display the differences between the end time stamp and start time stamp.
"""
print('How many problems of time stamps do you want to solve ?')
i = int(input())
input_timestamp = []
for i in range(1,i+1):
    ts = []
    print('Enter the Start time stamp & End time stamp in the form of dd-hh-mm-ss separated by space for case {}'.format(i))
    ts = input().split()   
    input_timestamp.append(ts)


def duration(ts):
    t1, t2, t = 0, 0, 0
    result_timestamp = []
    t1 = int(ts[0])*86400 + int(ts[1])*3600 + int(ts[2])*60 + int(ts[3])
    t2 = int(ts[4])*86400 + int(ts[5])*3600 + int(ts[6])*60 + int(ts[7])
    t = t2 - t1
    if t >= 86400:
        q = t//86400
        result_timestamp.append(q)
        r = t % 86400
        t = r
    else:
        result_timestamp.append(0)
        
    if t >=3600:
        q = t//3600
        result_timestamp.append(q)
        r = t % 3600
        t = r
    else:
        result_timestamp.append(0)
        
        
    if t >=60:
        q = t//60
        result_timestamp.append(q)
        r = t % 60
        t = r  
    else:
        result_timestamp.append(0)
        
    if t>= 0:
        result_timestamp.append(t)
    
    return(result_timestamp)
    
output_timestamp = []    
for ts in input_timestamp:
    output_timestamp.append(duration(ts))
print('The difference in the End Time Stamp and the Start Time Stamp in the array is ',output_timestamp)
    