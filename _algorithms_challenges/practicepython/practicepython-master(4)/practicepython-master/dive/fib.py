def fib(n):
    """this method returns sum of n natural numbers"""
    print "n = ",n
    if n > 1 :
        return n * fib(n-1)
    else:
        print "end of line"
        return 1



if __name__=="__main__":
    print fib(5)
