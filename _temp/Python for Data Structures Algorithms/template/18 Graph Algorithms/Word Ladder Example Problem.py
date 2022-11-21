# Word Ladder Example Code
# Below is the Vertex and Graph class used for the Word Ladder example code:

c_ Vertex:
    ___ - key
        id _ key
        connectedTo _     # dict

    ___ addNeighbornbr,weight_0
        connectedTo[nbr] _ weight

    ___ __str__ 
        r_ s..(id) + ' connectedTo: ' + s..([x.id ___ x __ connectedTo])

    ___ getConnections 
        r_ connectedTo.keys()

    ___ getId 
        r_ id

    ___ getWeightnbr
        r_ connectedTo[nbr]

c_ Graph:
    ___ -  
        vertList _     # dict
        numVertices _ 0

    ___ addVertexkey
        numVertices _ numVertices + 1
        newVertex _ Vertex(key)
        vertList[key] _ newVertex
        r_ newVertex

    ___ getVertexn
        __ n __ vertList:
            r_ vertList[n]
        ____
            r_ N..

    ___ __contains__n
        r_ n __ vertList

    ___ addEdgef,t,cost_0
        __ f n.. __ vertList:
            nv _ addVertex(f)
        __ t n.. __ vertList:
            nv _ addVertex(t)
        vertList[f].addNeighbor(vertList[t], cost)

    ___ getVertices 
        r_ vertList.keys()

    ___ -i.. 
        r_ iter(vertList.v..

# Code for buildGraph function:

___ buildGraph(wordFile
    d _     # dict
    g _ Graph()

    wfile _ open(wordFile,'r')
    # create buckets of words that differ by one letter
    ___ line __ wfile:
        print line
        word _ line[:-1]
        print word
        ___ i __ r..(l..(word
            bucket _ word[:i] + '_' + word[i+1:]
            __ bucket __ d:
                d[bucket].a..(word)
            ____
                d[bucket] _ [word]
    # add vertices and edges for words in the same bucket
    ___ bucket __ d.keys(
        ___ word1 __ d[bucket]:
            ___ word2 __ d[bucket]:
                __ word1 !_ word2:
                    g.addEdge(word1,word2)
    r_ g

# Please reference the video for full explanation!