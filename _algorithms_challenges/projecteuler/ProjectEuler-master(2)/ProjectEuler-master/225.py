import sys
    
def has_divisor(d):
    remainder_hash = set()
    T = (1, 1, 1)
    while True:
        T = (T[1], T[2], (T[0] + T[1] + T[2]) % d)
        if T[2] is 0:
            return True
        hash_value = T[0]*d*d + T[1]*d + T[2]
        if hash_value in remainder_hash:
            return False
        else:
            remainder_hash.add(hash_value)
    
def main():
    count = 0
    for d in range(1, 10000, 2):
        if not has_divisor(d):
            count += 1
            print('''%d: %d''' % (count, d))
            if count is 124:
                break
        
if __name__ == '__main__':
    sys.exit(main())
