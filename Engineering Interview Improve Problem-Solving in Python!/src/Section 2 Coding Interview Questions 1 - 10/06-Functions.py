
def d(start):
    def inner():
        nonlocal start
        start += 1
        print(start)
    return inner

f = d(10)

f() # 11 will be printed
f() # 12 will be printed
