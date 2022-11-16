c_ Solution:
    ___ validMountainArray A: List[int]) -> bool:
        __(len(A)<3
            r_ False
        
        i _ 1
        _____(i<len(A) and A[i]>A[i-1]
            i+_1
        
        __(i==1 or i==len(A)):
            r_ False
        
        _____(i<len(A) and A[i]<A[i-1]
            i+_1
        
        r_ i==len(A)