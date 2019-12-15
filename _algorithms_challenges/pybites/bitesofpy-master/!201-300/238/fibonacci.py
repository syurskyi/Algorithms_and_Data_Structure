def fib(n):
   if n < 0:
        raise ValueError
   elif n in (0, 1):
       return n
   else:
       return(fib(n-1) + fib(n-2))