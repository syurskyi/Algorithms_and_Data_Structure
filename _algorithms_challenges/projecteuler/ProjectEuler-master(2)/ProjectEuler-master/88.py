import sys

PROBLEM_BOUND = 12000

product_sum_set_cache = {}

def init_product_sum_set(number):
    if number in product_sum_set_cache:
        return
    product_sum_set_cache[number] = set()
    for d in range(2, number + 1):
        if d * d > number:
            break
        q, r = divmod(number, d)
        if r != 0:
            continue
        k = number - d - q + 2
        product_sum_set_cache[number].add(k)
        for i in product_sum_set_cache[q]:
            product_sum_set_cache[number].add(k + i - 1)
    
def main():
    min_product_sum = [2*n for n in range(PROBLEM_BOUND + 1)]
    for n in range(2, 2 * PROBLEM_BOUND + 1):
        init_product_sum_set(n)
    for n in product_sum_set_cache:
        for k in product_sum_set_cache[n]:
            if k <= PROBLEM_BOUND and n < min_product_sum[k]:
                min_product_sum[k] = n
    print(sum(set(min_product_sum[2::])))

if __name__ == '__main__':
    sys.exit(main())
