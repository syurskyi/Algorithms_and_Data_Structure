c_ Solution:
    ___ fourSumCount A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
      m _ {}
      ans _ 0

      ___ i __ range(0,l..(A)):
        x _ A[i]
        ___ j __ range(0,l..(B)):
          y _ B[j]
          __(x+y n.. __ m
            m[x+y] _ 0
          m[x+y]+_1

      ___ i __ range(0,l..(C)):
        x _ C[i]
        ___ j __ range(0,l..(D)):
          y _ D[j]
          target _ -(x+y)
          __(target __ m
            ans+_m[target]

      r_ ans