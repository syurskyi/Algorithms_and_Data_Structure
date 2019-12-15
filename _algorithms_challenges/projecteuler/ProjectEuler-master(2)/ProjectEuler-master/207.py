import sys
                        
def main():
    power2 = set(2**i for i in range(20))
    good_count = 0
    for a in range(1, 2**19):
        if a + 1 in power2:
            good_count += 1
        if good_count * 12345 < a:
            print('''P(%d) = %d/%d''' % (a*(a+1), good_count, a))
            break
        
if __name__ == '__main__':
    sys.exit(main())
