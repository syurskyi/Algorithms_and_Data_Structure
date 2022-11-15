import time

def recur_countdown_timer(n):
    if n == 0:
        return n
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_timer(n-1)

def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)

z = 5
print(f"Counting down from {z}:")
# iter_countdown_timer(z)
print(recur_countdown_timer(z))
