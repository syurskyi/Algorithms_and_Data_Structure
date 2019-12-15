def volume_of_box(sizes):
    index = 0
    output = 1
    for i in sizes:
        output *= sizes[i]
    return output
