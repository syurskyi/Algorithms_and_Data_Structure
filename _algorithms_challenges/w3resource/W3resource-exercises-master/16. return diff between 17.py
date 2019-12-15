def difference():
    n = int(input("Enter a number to calc diff from 17, double if its over: "))
    if n > 17:
        print((n - 17) * 2)
    else:
        print(17 - n)
difference()