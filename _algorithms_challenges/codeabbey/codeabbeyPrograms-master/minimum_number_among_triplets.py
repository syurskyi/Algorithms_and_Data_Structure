
"""
Created on Tue Apr 26 17:35:23 2016

@author: rajan gyawali

problem 5

Several triplets of numbers are given to you. Your task is to select minimum among each of triplets.

"""

print('Enter the numbers for triplets separated by space')
num = input()
array = num.split()
l = len(array)
result = []
i = 0
while i < l:
    a = []
    a = array[i:i+3]
    result.append(a)
    i += 3
print(result)
out = []
for a in result:
    small = float(a[0])
    for i in range(1,3):
        if small > float(a[i]):
            small = float(a[i])
        i += 1
    out.append(small)
print('The minimum of each triplet array is ',out)
    
    