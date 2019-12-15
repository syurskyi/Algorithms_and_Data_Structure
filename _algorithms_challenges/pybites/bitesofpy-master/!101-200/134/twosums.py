def two_sums(numbers: list, target: int):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    num_list = sorted(enumerate(numbers), key=lambda x: x[1])
    for x in range(len(numbers)):
        i, n = num_list[x]
        for j, m in num_list[x + 1:]:
            n_m = n + m
            if n_m == target:
                return (i, j)
            if n_m > target:
                break
    return None
