def solve_recursion(self, m, w, v, n):
    # base cases
    if n == 0 or m == 0:
        return 0

    # the given item can NOT fit into the knapsack
    if w[n - 1] > m:
        return self.solve_recursion(m, w, v, n - 1)
    else:
        # given item can fit into the knapsack so we have 2 options (include, exclude)
        n_included = v[n - 1] + self.solve_recursion(m - w[n - 1], w, v, n - 1)
        n_excluded = self.solve_recursion(m, w, v, n - 1)

        return max(n_included, n_excluded)