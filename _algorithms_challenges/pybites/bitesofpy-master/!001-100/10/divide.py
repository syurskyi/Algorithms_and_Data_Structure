def positive_divide(numerator, denominator):
    if denominator == 0:
        return 0
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError()
    except TypeError as e:
        raise e
    return result
