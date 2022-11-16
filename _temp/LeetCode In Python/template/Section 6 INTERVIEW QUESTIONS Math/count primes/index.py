c_ Solution:
    ___ countPrimes n: i..) -> i..:
        
        __ n<2:
            r_ 0
        isPrime _ [T..]*n
        isPrime[0] _ isPrime[1] _ F..
        
        ___ i __ r..(2,math.ceil(math.sqrt(n))):
            __ isPrime[i]:
                ___ multiples_of_i __ r..(i*i,n,i
                    isPrime[multiples_of_i] _ F..
        
        r_ sum(isPrime)