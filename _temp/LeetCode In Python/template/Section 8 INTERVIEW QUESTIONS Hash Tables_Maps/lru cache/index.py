from collections import deque


c_ LRUCache:

    ___ -  capacity: int
        c _ capacity
        m _ dict()
        deq _ deque()

    ___ get key: int) -> int:
        __ key __ m:
            value _ m[key]
            deq.remove(key)
            deq.a..(key)
            r_ value
        ____
            r_ -1

    ___ put key: int, value: int) -> N..:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        __ key n.. __ m:
            __ l..(deq) __ c:
                oldest _ deq.popleft()
                d.. m[oldest]
        ____
            deq.remove(key)

        m[key] _ value
        deq.a..(key)
