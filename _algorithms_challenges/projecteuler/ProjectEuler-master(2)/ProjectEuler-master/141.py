# [6230016, 36869184, 16900, 12551169024, 1361388609, 9, 1380568336, 13855173264, 70963776, 256160025, 10404, 97344, 37344321, 547674002500, 8534988225, 9729849600, 16394241600, 123383587600, 12006225, 142965659664, 7322436, 196112016, 576081]
import math
import sys
      
def main():
    squares = set(i*i for i in range(1, 1000000))
    results = []
    for d in range(1, 1000000):
        d2 = d*d
        for q in range(1, d+1):
            if d2 % q == 0:
                n = d*int(d2/q) + q
                if n in squares:
                    results.append(n)
                    print(n)
    unique_results = list(set(results))
    print(unique_results)
    print(sum(unique_results))

if __name__ == '__main__':
    sys.exit(main())
