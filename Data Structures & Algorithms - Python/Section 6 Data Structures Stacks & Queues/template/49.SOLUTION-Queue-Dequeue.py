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
        r.. T..

    ___ dequeue
        __ length __ 0
            r.. N..
        temp = first
        __ length __ 1
            first = N..
            last = N..
        ____
            first = first.next
            temp.n.. _ N..
        length -= 1
        r.. temp

 

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value
# (0) Items - Returns None
print(my_queue.dequeue())



"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""