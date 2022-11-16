c_ QueueLine:
	___ -  
        q _ []
    
    ___ enqueue x: int) -> N..:
        q.append(x)


    ___ dequeue ) -> N..:
        __(len(q) > 0
            q.pop(0)

    ___ front ) -> int:
        __(len(q) == 0
            r_ N..

        r_ q[0]