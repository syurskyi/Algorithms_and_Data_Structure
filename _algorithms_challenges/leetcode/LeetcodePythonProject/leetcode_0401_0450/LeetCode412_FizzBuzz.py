'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for num in range(1, n+1):
            if num % 15 == 0:
                result.append('FizzBuzz')
            elif num % 5 == 0:
                result.append('Buzz')
            elif num % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(num))
        return result
