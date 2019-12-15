def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance is only defined for sequences of equal length")
    return sum([1 for i in range(len(strand_a)) if strand_a[i] != strand_b[i]])
