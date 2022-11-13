c_ Node
    ___ -  value
        ? _ ?
        n.. _ N..
        

c_ Queue
    ___ -  value
        n... _ ? ?
        first _ ?
        last _ ?
        length = 1

    ___ print_queue
        temp = first
        _____  ? __ n.. N..
            print ?.v..
            ? _ ?.n..
        
    ___ enqueue value
        n... _ ? ?
        __ first is N..
            first _ ?
            last _ ?
        ____
            last.next _ ?
            last _ ?
        length += 1
        



my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()



"""
    EXPECTED OUTPUT:
    ----------------
    Queue before enqueue(2):
    1

    Queue after enqueue(2):
    1
    2

"""