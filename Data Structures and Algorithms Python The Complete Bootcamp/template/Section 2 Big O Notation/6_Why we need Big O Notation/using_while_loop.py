import time
time.time()

timestamp1 = time.time()

# Sum of natural numbers up to num
num = 100
__ num < 0:
   print("Enter a positive number")
____
   sum = 0
   # use while loop to iterate until zero
   ______(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

### Program Completed ###

timestamp2 = time.time()
print((timestamp2 - timestamp1))