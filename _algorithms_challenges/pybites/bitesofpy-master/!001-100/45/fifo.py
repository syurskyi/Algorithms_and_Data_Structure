from collections import deque


def my_queue(n=5):
    return deque(maxlen=n)


if __name__ == '__main__':
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))

    """Queue size does not go beyond n int, this outputs:
    (0, [0])
    (1, [0, 1])
    (2, [0, 1, 2])
    (3, [0, 1, 2, 3])
    (4, [0, 1, 2, 3, 4])
    (5, [1, 2, 3, 4, 5])
    (6, [2, 3, 4, 5, 6])
    (7, [3, 4, 5, 6, 7])
    (8, [4, 5, 6, 7, 8])
    (9, [5, 6, 7, 8, 9])
    """
