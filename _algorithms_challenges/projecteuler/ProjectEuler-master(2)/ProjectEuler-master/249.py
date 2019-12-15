import sys

SIEVE_RANGE = 1550000
PROBLEM_MOD = 10**16

sieve = [False] * SIEVE_RANGE
primes = []
coins = []

def init_primes():
    sieve[0], sieve[1] = True, True
    for i in range(2, SIEVE_RANGE):
        if sieve[i] is False:
            primes.append(i)
            for j in range(i+i, SIEVE_RANGE, i):
                sieve[j] = True

def init_coins(coin_range):
    for i in range(len(primes)):
        if primes[i] > coin_range:
            break
        coins.append(primes[i])

def get_coin_change_ways():
    ways = [0] * SIEVE_RANGE
    ways[0] = 1
    for c in coins:
        for j in range(SIEVE_RANGE-1, -1, -1):
            if j+c < SIEVE_RANGE:
                ways[j+c] = (ways[j+c] + ways[j]) % PROBLEM_MOD
                
    total_ways = 0
    for i in range(len(ways)):
        if sieve[i] is False:
            total_ways += ways[i]
    total_ways %= PROBLEM_MOD
    print(total_ways)
            
def main():
    init_primes()
    init_coins(5000)
    get_coin_change_ways()

if __name__ == '__main__':
    sys.exit(main())
