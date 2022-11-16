# network delay time - leetcode
c_ Solution:
    ___ networkDelayTime times: List[List[int]], N: int, K: int) -> int:

        g _ collections.defaultdict(list)
        ___ u, v, cost __ times:
            g[u].a..((cost, v))

        # cost,node
        min_heap _ [(0, K)]
        visited _ set()
        distance _ {i: float('inf') ___ i __ range(1, N+1)}
        distance[K] _ 0

        _____ min_heap:
            cur_dist, u _ heapq.heappop(min_heap)
            __ u __ visited:
                continue
            visited.add(u)
            __ l..(visited) __ N:
                r_ cur_dist

            ___ direct_distance, v __ g[u]:
                __ cur_dist + direct_distance < distance[v] and v n.. __ visited:
                    distance[v] _ cur_dist + direct_distance
                    heapq.heappush(min_heap, (cur_dist + direct_distance, v))
        r_ -1
