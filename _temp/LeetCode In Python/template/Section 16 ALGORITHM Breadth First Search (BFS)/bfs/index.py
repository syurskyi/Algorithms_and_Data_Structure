
____ collections ______ defaultdict


c_ Graph:

    ___ -
        graph _ defaultdict(list)

    ___ setEdge u, v
        graph[u].a..(v)

    ___ bfs s
        visited _ s..

        queue _    # list
        queue.a..(s)

        visited.add(s)

        _____ queue:
            u _ queue.p.. 0)
            print(u, end_" ")

            ___ v __ graph[u]:
                __ v n.. __ visited:
                    queue.a..(v)
                    visited.add(v)


g _ Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.bfs(2)
