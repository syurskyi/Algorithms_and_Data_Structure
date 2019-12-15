# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:18:26 2016

@author: rajan gyawali

Fibonacci numbers module

"""

def fib(n):
    a,b = 0,1
    print(a)
    while b<n:
        print(b, end = ' ')
        a, b = b, a+b
        print()
        
def fib2(n):
    result = [] 
    a,b = 0, 1
    result.append(a)
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
    