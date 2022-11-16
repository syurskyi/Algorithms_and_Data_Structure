# Knight's Tour Code
#
# ** Below is th ecode referenced in the video lecture. Please refer to the video lectures for full explanation.**

___ knightGraph(bdSize
    ktGraph _ Graph()
    ___ row __ range(bdSize
        ___ col __ range(bdSize
            nodeId _ posToNodeId(row,col,bdSize)
            newPositions _ genLegalMoves(row,col,bdSize)
            ___ e __ newPositions:
                nid _ posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid)
    r_ ktGraph

___ posToNodeId(row, column, board_size
    r_ (row * board_size) + column

___ genLegalMoves(x,y,bdSize
    newMoves _ []
    moveOffsets _ [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    ___ i __ moveOffsets:
        newX _ x + i[0]
        newY _ y + i[1]
        __ legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize
            newMoves.append((newX,newY))
    r_ newMoves

___ legalCoord(x,bdSize
    __ x >_ 0 and x < bdSize:
        r_ True
    ____
        r_ False

___ knightTour(n,path,u,limit
        u.setColor('gray')
        path.append(u)
        __ n < limit:
            nbrList _ list(u.getConnections())
            i _ 0
            done _ False
            _____ i < len(nbrList) and n.. done:
                __ nbrList[i].getColor() == 'white':
                    done _ knightTour(n+1, path, nbrList[i], limit)
                i _ i + 1
            __ n.. done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        ____
            done _ True
        r_ done