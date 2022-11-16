# Knight's Tour Code
#
# ** Below is th ecode referenced in the video lecture. Please refer to the video lectures for full explanation.**

___ knightGraph(bdSize
    ktGraph _ Graph()
    ___ row __ r..(bdSize
        ___ col __ r..(bdSize
            nodeId _ posToNodeId(row,col,bdSize)
            newPositions _ genLegalMoves(row,col,bdSize)
            ___ e __ newPositions:
                nid _ posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    r_ ktGraph

___ posToNodeId(row, column, board_size
    r_ (row * board_size) + column

___ genLegalMoves(x,y,bdSize
    newMoves _    # list
    moveOffsets _ [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    ___ i __ moveOffsets:
        newX _ x + i[0]
        newY _ y + i[1]
        __ legalCoord(newX,bdSize) ___ \
                        legalCoord(newY,bdSize
            newMoves.a..((newX,newY))
    r_ newMoves

___ legalCoord(x,bdSize
    __ x >_ 0 ___ x < bdSize:
        r_ T..
    ____
        r_ F..

___ knightTour(n,path,u,limit
        u.setColor('gray')
        path.a..(u)
        __ n < limit:
            nbrList _ list(u.getConnections())
            i _ 0
            done _ F..
            _____ i < l..(nbrList) ___ n.. done:
                __ nbrList[i].getColor() __ 'white':
                    done _ knightTour(n+1, path, nbrList[i], limit)
                i _ i + 1
            __ n.. done:  # prepare to backtrack
                path.p.. 
                u.setColor('white')
        ____
            done _ T..
        r_ done