#!/usr/bin/env python

"""Problem 88: Product-sum numbers"""

from math import sqrt


def main():
    # the minimal product-sum for some k is between k and 2k
    # 2k is a guaranteed solution as the set {2, k} can be padded with k-2 ones

    K = 12000 # maximum k
    N = K*2   # limit for product sum

    min_product_sums = [N]*(K+1)
    min_product_sums[:2] = 0, 0

    def search(product, sum_, num_factors, max_factor):
        k = product - sum_ + num_factors

        if k > K:
            return

        if product < min_product_sums[k]:
            min_product_sums[k] = product

        for factor in range(max_factor, N//product+1):
            search(product*factor, sum_+factor, num_factors+1, factor)

    for factor in range(2, int(sqrt(N)) + 1):
        search(factor, factor, 1, factor)

    return sum(set(min_product_sums))


if __name__ == "__main__":
    print(main())
