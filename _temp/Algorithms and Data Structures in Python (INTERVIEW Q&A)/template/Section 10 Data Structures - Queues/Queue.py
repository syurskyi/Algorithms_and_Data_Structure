
c_ Queue:

    ? ? - 
        queue _ []

    # O(1) running time
    ? ? is_empty
        r_ queue __ []

    # O(1) running time
    ? ? enqueue data
        queue.append(data)

    # O(N) linear running time but we could use doubly linked list
    # to achieve O(1) for all operations
    ? ? dequeue
        data _ queue[0]
        del queue[0]
        r_ data

    # O(1) constant running time
    ? ? peek
        r_ queue[0]

    # O(1)
    ? ? size_queue
        r_ l..(queue)
