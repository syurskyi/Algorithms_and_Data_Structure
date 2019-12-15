# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:04:02 2016

@author: rajan gyawali

Problem #16

Average of numbers

Input data will give the number of test-cases in the first line.
Then test-cases themselves will follow, one case per line.
Each test-case describes an array of positive integers with value of 0 marking end. 
(this zero should not be included into calculations!!!).
Answer should contain average values for each array, 
rounded to nearest integer , separated by spaces.
"""

print('How many cases do you want ?')
n = int(input())
print('Enter the cases in different line terminated by a zero')
test_cases = []
for i in range(0,n):
    line = input()
    test_cases.append(line)
    
text = ' '.join(test_cases)
text = text.split()

    

newlist = []
newlist1 = []
for i in text:
    
    if i == '0':
        newlist.append(newlist1)
        newlist1 = []
        continue
    else:
        newlist1.append(i)
    
print(newlist)

result_list = []
rounded_result = []
for n in newlist:
    avg = 0
    s = 0
    for i in range(0,len(n)):
        s += float(n[i])
        avg = s/len(n)
    result_list.append(avg)
    rounded_result.append(round(avg,0))

print('The average of the numbers in each test cases are as follows ',result_list)

print('The rounded test result is ',rounded_result)
        
    
