c_ Solution
    dx _ [0, 0, -1, 1]
    dy _ [1, -1, 0, 0]

    ___ solution board, word, x, y, cur
        __(x < 0 __ x >_ l..(board) __ y < 0 __ y >_ l..(board[x]) __ board[x][y] __ ' '
            r_ F..
        cur +_ board[x][y]

        __(l..(cur) > l..(word
            r_ F..
        __(cur[l..(cur)-1] !_ word[l..(cur)-1]
            r_ F..
        __(cur __ word
            r_ T..

        temp _ board[x][y]
        board[x][y] _ ' '

        ___ i __ r..(4
            __(solution(board, word, x+dx[i], y+dy[i], cur
                r_ T..

        board[x][y] _ temp
        r_ F..

    ___ exist board: List[List[s..]], word: s..) __ b..:
        __(l..(word) __ 0
            r_ T..
        n _ l..(board)
        ___ i __ r..(n
            m _ l..(board[i])
            ___ j __ r..(m
                __(word[0] __ board[i][j] ___ solution(board, word, i, j, ""
                    r_ T..
        r_ F..
