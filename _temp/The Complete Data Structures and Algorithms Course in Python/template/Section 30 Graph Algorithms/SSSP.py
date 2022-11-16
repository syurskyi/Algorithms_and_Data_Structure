#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


c_ Graph:
    ___ -  gdict_None
        __ gdict __ N..:
            gdict _     # dict
        gdict _ gdict
    
    ___ bfs start, end
        queue _    # list
        queue.a..([start])
        _____ queue:
            path _ queue.p.. 0)
            node _ path[-1]
            __ node __ end:
                r_ path
            ___ adjacent __ gdict.get(node,    # list
                new_path _ list(path)
                new_path.a..(adjacent)
                queue.a..(new_path)

customDict _ { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g _ Graph(customDict)
print(g.bfs("a", "e"))
