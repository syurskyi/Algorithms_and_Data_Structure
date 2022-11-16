# Implementation of Breadth First Search
# An alternative algorithm called Breath-First search provides us with the ability to return the same results
# as DFS but with the added guarantee to return the shortest-path first. This algorithm is a little more tricky
# to implement in a recursive manner instead using the queue data-structure, as such I will only being documenting
# the iterative approach. The actions performed per each explored vertex are the same as the depth-first implementation,
# however, replacing the stack with a queue will instead explore the breadth of a vertex depth before moving on.
# This behavior guarantees that the first path located is one of the shortest-paths present, based on number
# of edges being the cost factor.
#
# We'll assume our Graph is in the form:

graph _ {'A': s..(['B', 'C']),
         'B': s..(['A', 'D', 'E']),
         'C': s..(['A', 'F']),
         'D': s..(['B']),
         'E': s..(['B', 'F']),
         'F': s..(['C', 'E'])}

# Connected Component
#
# Similar to the iterative DFS implementation the only alteration required is to remove the next item from
# the beginning of the list structure instead of the stacks last.

___ bfs(graph, start
    visited, queue _ s.., [start]
    _____ queue:
        vertex _ queue.p.. 0)
        __ vertex n.. __ visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    r_ visited

bfs(graph, 'A')
# {'A', 'B', 'C', 'D', 'E', 'F'}
#
# Paths
#
# This implementation can again be altered slightly to instead return all possible paths between two vertices,
# the first of which being one of the shortest such path.

___ bfs_paths(graph, start, goal
    queue _ [(start, [start])]
    _____ queue:
        (vertex, path) _ queue.p.. 0)
        ___ next __ graph[vertex] - s..(path
            __ next __ goal:
                yield path + [next]
            ____
                queue.a..((next, path + [next]))

list(bfs_paths(graph, 'A', 'F'))
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
#
# Knowing that the shortest path will be returned first from the BFS path generator method we can create
# a useful method which simply returns the shortest path found or None if no path exists. As we are using a generator
# this in theory should provide similar performance results as just breaking out and returning the first matching path
# in the BFS implementation.

___ shortest_path(graph, start, goal
    try:
        r_ next(bfs_paths(graph, start, goal))
    except StopIteration:
        r_ N..

shortest_path(graph, 'A', 'F')
# ['A', 'C', 'F']
#
# Resources