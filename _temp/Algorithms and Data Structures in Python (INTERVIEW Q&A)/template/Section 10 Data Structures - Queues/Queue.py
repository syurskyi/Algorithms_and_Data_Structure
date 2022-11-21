
class Queue:

    ? ? __init__(self):
        self.queue _ []

    # O(1) running time
    ? ? is_empty(self):
        r_ self.queue __ []

    # O(1) running time
    ? ? enqueue(self, data):
        self.queue.append(data)

    # O(N) linear running time but we could use doubly linked list
    # to achieve O(1) for all operations
    ? ? dequeue(self):
        data _ self.queue[0]
        del self.queue[0]
        r_ data

    # O(1) constant running time
    ? ? peek(self):
        r_ self.queue[0]

    # O(1)
    ? ? size_queue(self):
        r_ l..(self.queue)
