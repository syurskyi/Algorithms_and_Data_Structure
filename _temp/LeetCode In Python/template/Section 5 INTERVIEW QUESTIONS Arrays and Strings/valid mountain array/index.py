c_ Solution:
    ___ validMountainArray A: List[int]) -> bool:
        __(l..(A)<3
            r_ False
        
        i _ 1
        _____(i<l..(A) and A[i]>A[i-1]
            i+_1
        
        __(i__1 or i__len(A)):
            r_ False
        
        _____(i<l..(A) and A[i]<A[i-1]
            i+_1
        
        r_ i__len(A)