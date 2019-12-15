import sys

A = '''1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'''
B = '''8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'''
L = len(A)
fibonacci = []

def init_fibonacci():
    prev, curr = 0, 1
    while curr < 100000000000000000:
        fibonacci.append(curr)
        prev, curr = curr, prev + curr   
   
def d(n):
    return get_digit(n, get_which_word(n))
   
def get_which_word(n):
    n0 = n - 1
    for i in range(len(fibonacci)):
        if fibonacci[i] * L > n0:
            return i
    return -1

def get_digit(n, which_word):
    n0 = n - 1
    if which_word == 0:
        return A[n0]
    if which_word == 1:
        return B[n0]
    offset = (fibonacci[which_word - 2]) * L
    if n0 < offset:
        return get_digit(n, which_word - 2)
    else:
        return get_digit(n - offset, which_word - 1)
    return -1
    
def main():
    init_fibonacci()
    result = [d((127 + 19*n) * 7**n) for n in range(18)]
    print(''.join(result)[::-1])

if __name__ == '__main__':
    sys.exit(main())
