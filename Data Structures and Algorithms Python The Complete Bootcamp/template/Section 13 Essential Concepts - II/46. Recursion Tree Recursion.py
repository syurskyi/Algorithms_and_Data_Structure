def run(n):
    if n == 0:
        return
    print("")
    run(n-1)

run(3)

def run(n):
    if n == 0:
        return
    print(n)
    run(n-1)
    run(n-1)

run(3)