"""
How about writing a queue that holds the last 5 items?

Queue follows First-In-First-Out methodology, i.e., the data item stored first will be accessed first. A real-world example of queue can be a single-lane one-way road, where the vehicle enters first, exits first. More real-world examples can be seen as queues at the ticket windows and bus-stops. [source]
Complete the my_queue function to return a queue-like data type that keeps the last n items.

Check the standard library to see how you can do this in the shortest/most efficient way.

See an example output below and the tests that check for various values of n. Have fun!"""

import collections


def my_queue(n=5):
    mylist = collections.deque([],maxlen=n)
    return mylist


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