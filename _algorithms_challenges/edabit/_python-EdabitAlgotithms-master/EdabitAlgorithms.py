'''
These are solutions to some of the Python Edabit.com excercises.

***If you don't know, Edabit.com is a website in which you can practise algorithm-thinking and creation***

These solutions are not necesarily the "correct ones", but they're what I came up with
Obviously, they can be done in more efficient ways

If you have solutions, don't hesitate to collaborate

Enjoy!
'''

'''
The comments are the name of the problem.
'''

#Is the number even or odd?
def isEvenOrOdd(num):
  if (num % 2 == 0):
    return "even"
  else:
    return "odd"

#Return the last item in a list
def getLastItem(lst):
  return lst[-1]

#Find the LARGEST number in a list
def findLargestNum(nums):
	return max(nums)

#Check if number is 'less than' or 'equal' to zero
def lessThanOrEqualToZero(num):
  if (num <= 0):
    return True
  else:
    return False

#Find the SMALLEST number in a list
def findSmallestNum(lst):
  return min(lst)

 #Reverse the order of a string
 def reverse(s):
  return s[::-1]

#Eliminate all odd numbers within a list
def noOdds(lst):
    numbers_buf = lst[:]
    for item in lst:
        if item % 2:
            numbers_buf.remove(item)
    return numbers_buf

#Return the four letter strings
def isFourLetters(lst):
    return[i for i in lst if len(i)==4]
