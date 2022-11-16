c_ Solution:
    dx _ [0, 0, -1, 1]
    dy _ [1, -1, 0, 0]

    ___ solution board, word, x, y, cur
        __(x < 0 or x >_ len(board) or y < 0 or y >_ len(board[x]) or board[x][y] == ' '
            r_ False
        cur +_ board[x][y]

        __(len(cur) > len(word)):
            r_ False
        __(cur[len(cur)-1] !_ word[len(cur)-1]
            r_ False
        __(cur == word
            r_ True

        temp _ board[x][y]
        board[x][y] _ ' '

        ___ i __ range(4
            __(solution(board, word, x+dx[i], y+dy[i], cur)):
                r_ True

        board[x][y] _ temp
        r_ False

    ___ exist board: List[List[str]], word: str) -> bool:
        __(len(word) == 0
            r_ True
        n _ len(board)
        ___ i __ range(n
            m _ len(board[i])
            ___ j __ range(m
                __(word[0] == board[i][j] and solution(board, word, i, j, "")):
                    r_ True
        r_ False
