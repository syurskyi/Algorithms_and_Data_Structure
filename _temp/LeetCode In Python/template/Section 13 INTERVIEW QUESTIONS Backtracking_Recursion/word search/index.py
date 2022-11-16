c_ Solution:
    dx _ [0, 0, -1, 1]
    dy _ [1, -1, 0, 0]

    ___ solution board, word, x, y, cur
        __(x < 0 or x >_ l..(board) or y < 0 or y >_ l..(board[x]) or board[x][y] __ ' '
            r_ False
        cur +_ board[x][y]

        __(l..(cur) > l..(word)):
            r_ False
        __(cur[l..(cur)-1] !_ word[l..(cur)-1]
            r_ False
        __(cur __ word
            r_ True

        temp _ board[x][y]
        board[x][y] _ ' '

        ___ i __ range(4
            __(solution(board, word, x+dx[i], y+dy[i], cur)):
                r_ True

        board[x][y] _ temp
        r_ False

    ___ exist board: List[List[str]], word: str) -> bool:
        __(l..(word) __ 0
            r_ True
        n _ l..(board)
        ___ i __ range(n
            m _ l..(board[i])
            ___ j __ range(m
                __(word[0] __ board[i][j] and solution(board, word, i, j, "")):
                    r_ True
        r_ False
