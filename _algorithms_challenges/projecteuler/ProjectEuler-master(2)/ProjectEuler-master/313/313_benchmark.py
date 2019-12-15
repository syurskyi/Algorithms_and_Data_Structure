import sys

class Benchmark():
    def __init__(self):
        self.R = 'R'
        self.X = '_'
        self.B = 'B'

    def do(self):
        for m, n in [(2, 7), (7, 2)]:
            print(m, n, self.get_ways_naive(m, n), self.get_ways(m, n))

    def get_ways(self, m, n):
        m, n = min(m, n), max(m, n)
        if m == n:
            return 5 + (m - 2) * 8
        else:
            return 3 + (n - m) * 6 + (m - 2) * 8

    def get_ways_naive(self, m, n):
        initial_board = [[self.B for _ in range(m)] for _ in range(n)]
        initial_board[0][0] = self.R
        initial_board[n-1][m-1] = self.X
        
        visited_boards = set()
        
        bfs_queue = []
        bfs_queue.append([initial_board, 0])        
        while bfs_queue:
            board, steps = bfs_queue[0]
            bfs_queue.pop(0)
            hashed_board = self.hash_board(board)
            if hashed_board in visited_boards:
                continue
            visited_boards.add(hashed_board)
            if board[n-1][m-1] == self.R:
                return steps
            next_steps = steps + 1
            for next_board in self.next_board_iterator(board, m, n):
                bfs_queue.append([next_board, next_steps])
                    
    def next_board_iterator(self, board, m, n):
        empty_pos = self.get_empty_pos(board, m, n)
        
        # slide down
        sliding_pos = empty_pos[0], empty_pos[1] - 1
        if sliding_pos[1] >= 0:
            yield self.build_next_board(board, m, n, empty_pos, sliding_pos)

        # slide up
        sliding_pos = empty_pos[0], empty_pos[1] + 1
        if sliding_pos[1] < n:
            yield self.build_next_board(board, m, n, empty_pos, sliding_pos)

        # slide right
        sliding_pos = empty_pos[0] - 1, empty_pos[1]
        if sliding_pos[0] >= 0:
            yield self.build_next_board(board, m, n, empty_pos, sliding_pos)

        # slide left
        sliding_pos = empty_pos[0] + 1, empty_pos[1]
        if sliding_pos[0] < m:
            yield self.build_next_board(board, m, n, empty_pos, sliding_pos)

    def build_next_board(self, board, m, n, empty_pos, sliding_pos):
        next_board = self.clone_board(board, m, n)
        next_board[empty_pos[1]][empty_pos[0]] = next_board[sliding_pos[1]][sliding_pos[0]]
        next_board[sliding_pos[1]][sliding_pos[0]] = self.X
        return next_board

    def hash_board(self, board):
        return ''.join([''.join(board[_]) for _ in range(len(board))])

    def get_empty_pos(self, board, m, n):
        for i in range(m):
            for j in range(n):
                if board[j][i] == self.X:
                    return i, j

    def clone_board(self, board, m, n):
        rv = [[None for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rv[j][i] = board[j][i]
        return rv

def main():
    benchmark = Benchmark()
    benchmark.do()
    
if __name__ == '__main__':
    sys.exit(main())
