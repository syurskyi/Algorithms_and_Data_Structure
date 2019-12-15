import sys

fibonacci = []
T = {}
U = {}
S = {}

def init_fibonacci():
    prev, curr = 1, 1
    while curr < 10**20:
        fibonacci.append(curr)
        prev, curr = curr, prev + curr   

def init_digit_sum_table():
    T[1] = [0, 1]
    T[2] = [1, 0]
    U[1] = [0, 1]
    U[2] = [1, 0]
    for i in range(3, 100):
        T[i] = [T[i-1][0] + T[i-1][1], T[i-1][0]]
        U[i] = [U[i-1][0] + U[i-1][1], U[i-1][0] + T[i-1][0]]
    S[1] = 1
    for i in range(2, 100):
        S[i] = S[i-1] + U[i][0] + U[i][1]
        
def zeckendorf(n):
    if n == 0: 
        return [0]
    digits, d = [], n
    for s in fibonacci[::-1]:
        if s <= d:
            digits.append(1)
            d -= s
        else:
            digits.append(0)
    # Remove leading zeros
    while digits[0] == 0:
        digits.pop(0)
    return digits

def solve(n):
    total_sum = 0
    rep = zeckendorf(n)
    prev_ones_count = 0
    for i in range(len(rep)):
        if rep[i] == 1:
            total_sum += S[len(rep) - 1 - i] + 1
            total_sum += prev_ones_count * fibonacci[len(rep) - 1 - i]
            prev_ones_count += 1
    return total_sum
    
def main():
    init_fibonacci()
    init_digit_sum_table()
    print(solve(10**17 - 1))

if __name__ == '__main__':
    sys.exit(main())
