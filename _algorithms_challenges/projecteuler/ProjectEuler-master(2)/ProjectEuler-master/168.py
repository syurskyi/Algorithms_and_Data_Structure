import sys
    
def main():
    sum = 0
    for k in range(1, 100):
        for d in range(1, 10):
            for y in range(1, 10):
                x, r = divmod((10**k - d)*y, 10*d - 1)
                if r != 0 or x < 10**(k-1):
                    continue
                sum += 10*x + y
    print(sum % 10**5)    
    
if __name__ == '__main__':
    sys.exit(main())
