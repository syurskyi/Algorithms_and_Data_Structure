
def hanoi(disk, source, middle, destination):

    # this is the base case -index 0 is always the smallest plate
    # we manipulate the smallest plate in the base case
    if disk == 0:
        print('Disk %s from %s to %s' % (disk, source, destination))
        return

    hanoi(disk-1, source, destination, middle)
    # this is not necessarily the largest plate - this is not the plate 0
    print('Disk %s from %s to %s' % (disk, source, destination))
    hanoi(disk-1, middle, source, destination)


hanoi(20, 'A', 'B', 'C')
