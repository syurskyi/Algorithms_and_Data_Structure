'''
Created on Mar 22, 2018

@author: tongq
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False
        self.candidates = set()

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root1 = TreeNode('')
        self.root2 = TreeNode('')
        self.buildTree(self.root1, words, False)
        self.buildTree(self.root2, words, True)
    
    def buildTree(self, root, words, reverse):
        for i0, word in enumerate(words):
            if reverse:
                word = word[::-1]
            node = root
            node.candidates.add(i0)
            for i, c in enumerate(word):
                if c not in node.children:
                    node.children[c] = TreeNode('')
                node = node.children[c]
                node.candidates.add(i0)
                if i == len(word)-1:
                    node.isLeaf = True
    
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cand1 = self.helper(self.root1, prefix)
        cand2 = self.helper(self.root2, suffix[::-1])
        res = -1
        for i in cand1:
            if i in cand2:
                res = max(res, i)
        return res
    
    def helper(self, root, word):
        if not word:
            return root.candidates
        for i, c in enumerate(word):
            if c not in root.children:
                return set()
            root = root.children[c]
            if i == len(word)-1:
                return root.candidates

if __name__ == '__main__':
    wordFilter = WordFilter(["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"])
    res = wordFilter.f("","abaa")
    print('res: %s' % res)
