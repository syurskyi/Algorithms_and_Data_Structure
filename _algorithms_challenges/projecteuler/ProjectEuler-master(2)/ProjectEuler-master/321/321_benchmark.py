import sys

class Benchmark():
    def __init__(self):
        self.R = 'R'
        self.X = '_'
        self.B = 'B'

    def do(self):
        for n in range(1, 8):
            print(n, self.get_ways_naive(n))
            
    def get_ways_naive(self, n):
        initial_board = self.R * n + self.X + self.B * n
        final_board = initial_board[::-1]
        visited_boards = set()
        
        bfs_queue = []
        bfs_queue.append([initial_board, 0])        
        while bfs_queue:
            board, steps = bfs_queue[0]
            bfs_queue.pop(0)
            if board == final_board:
                return steps
            if board in visited_boards:
                continue
            visited_boards.add(board)
            next_steps = steps + 1
            for next_board in self.next_board_iterator(board):
                bfs_queue.append([next_board, next_steps])
                    
    def next_board_iterator(self, board):
        n = len(board)
        empty_pos = board.index(self.X)
        
        # move right counter 
        moving_pos = empty_pos - 1
        if moving_pos >= 0:
            yield board[:moving_pos] + board[moving_pos:empty_pos+1][::-1] + board[empty_pos+1:]
        
        # move left counter 
        moving_pos = empty_pos + 1
        if moving_pos < n:
            yield board[:empty_pos] + board[empty_pos:moving_pos+1][::-1] + board[moving_pos+1:]
        
        # jump right counter
        jumping_pos = empty_pos - 2
        if jumping_pos >= 0:
            yield board[:jumping_pos] + board[jumping_pos:empty_pos+1][::-1] + board[empty_pos+1:]
        
        # jump left counter
        jumping_pos = empty_pos + 2
        if jumping_pos < n:
            yield board[:empty_pos] + board[empty_pos:jumping_pos+1][::-1] + board[jumping_pos+1:]
        
def main():
    benchmark = Benchmark()
    benchmark.do()
    
if __name__ == '__main__':
    sys.exit(main())
