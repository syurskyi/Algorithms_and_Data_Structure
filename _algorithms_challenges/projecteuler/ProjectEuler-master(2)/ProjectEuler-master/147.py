import sys

M, N = 47, 43

def is_out_of_bound(m, n, x, y):
    return x + y < n or x + y > 2 * m + n or x - y > n or y - x > n

def get_rectangle_count(m, n):
    count = int((m+1)*m/2) * int((n+1)*n/2)     
    d = m + n
    for x_begin in range(d + 1):
        for y_begin in range(d + 1):
            if is_out_of_bound(m, n, x_begin, y_begin):
                continue
            for x_end in range(x_begin + 1, d + 1):
                if is_out_of_bound(m, n, x_end, y_begin):
                    continue
                for y_end in range(y_begin + 1, d + 1):
                    if is_out_of_bound(m, n, x_begin, y_end) or is_out_of_bound(m, n, x_end, y_end):
                        continue 
                    count += 1
    return count
    
def main():
    sum = 0
    count_cache = {}
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if (m, n) not in count_cache:
                count_cache[(m, n)] = get_rectangle_count(m, n)
                count_cache[(n, m)] = count_cache[(m, n)]
            sum += count_cache[(m, n)]
            print(m, n, '=>', count_cache[(m, n)])
    print(sum)
            
if __name__ == '__main__':
    sys.exit(main())
