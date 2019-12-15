'''
Created on Feb 19, 2017

@author: MT
'''

class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = {}
        self.isLeaf = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        children = self.root.children
        for i, c in enumerate(word):
            if c in children:
                t = children[c]
            else:
                t = TrieNode(c)
                children[c] = t
            children = t.children
            if i == len(word)-1:
                t.isLeaf = True
    
    def searchDFS(self, children, word, startInd):
        if startInd == len(word):
            return bool(not children)
        c = word[startInd]
        if c in children:
            if startInd == len(word)-1 and children[c].isLeaf:
                return True
            return self.searchDFS(children[c].children, word, startInd+1)
        elif c == '.':
            for key, node in children.iteritems():
                if startInd == len(word)-1 and node.isLeaf:
                    return True
                if self.searchDFS(children[key].children, word, startInd+1):
                    return True
            return False
        else:
            return False
    
    def search(self, word):
        return self.searchDFS(self.root.children, word, 0)
    