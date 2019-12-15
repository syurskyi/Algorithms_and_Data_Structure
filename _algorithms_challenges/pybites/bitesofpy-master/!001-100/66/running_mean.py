def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sum_x = c = 0
    for x in sequence:
        c += 1
        sum_x += x
        yield round(float(sum_x)/c,2)
