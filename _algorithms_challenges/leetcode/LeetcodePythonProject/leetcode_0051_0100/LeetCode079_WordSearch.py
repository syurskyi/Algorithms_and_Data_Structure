'''
Created on Jan 24, 2017

@author: MT
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.helper(board, word, 0, i, j):
                    return True
        return False
    
    def helper(self, board, word, start, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if word[start] == board[i][j]:
            if start == len(word)-1:
                return True
            tmp = board[i][j]
            board[i][j] = '#'
            result = False
            if self.helper(board, word, start+1, i+1, j) or\
                self.helper(board, word, start+1, i, j+1) or\
                self.helper(board, word, start+1, i-1, j) or\
                self.helper(board, word, start+1, i, j-1):
                result = True
            board[i][j] = tmp
            if result:
                return True
        return False
    
    def test(self):
        board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E'],
        ]
        words = [
            'ABCCED',
            'SEE',
            'ABCB',
        ]
#         board = [
#             ['a'],
#         ]
#         words = [
#             'a',
#         ]
        for word in words:
            print('word: %s' % (word))
            result = self.exist(board, word)
            print('result: %s' % (result))
            print('-='*15+'-')
        

if __name__ == '__main__':
    Solution().test()
