import math
def Fibonacci():
    phiP = (1+math.sqrt(5))/2.0
    phiN = (1-math.sqrt(5))/2.0
    fib= lambda n: math.ceil((phiP**n -phiN**2)/(phiP -phiN))
    girdi=int(input("which fib series?"))
    sonuc=fib(girdi)
    print(sonuc)
    return sonuc
