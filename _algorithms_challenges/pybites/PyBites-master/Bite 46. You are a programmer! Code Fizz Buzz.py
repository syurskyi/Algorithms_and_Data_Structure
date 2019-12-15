"""Here is a beginner Bite to write Fizz Buzz:

Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", and any number divisible by five with the word "buzz".
...
For example, a typical round of fizz buzz would start as follows:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ..
Complete the fizzbuzz function below, it should take a number and return the right str or int.

If you want to write this TDD-style, consider doing Code Challenge 45 instead.

See also Coding Horror's Why Can't Programmers.. Program? for a fun read."""


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizz Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else: 
        return num
