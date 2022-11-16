c_ Solution:
    ___ countPrimes n: int) -> int:
        
        __ n<2:
            r_ 0
        isPrime _ [True]*n
        isPrime[0] _ isPrime[1] _ False
        
        ___ i __ range(2,math.ceil(math.sqrt(n))):
            __ isPrime[i]:
                ___ multiples_of_i __ range(i*i,n,i
                    isPrime[multiples_of_i] _ False
        
        r_ sum(isPrime)