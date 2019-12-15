'''
Created on Feb 18, 2017

@author: MT
'''

class TrieNode(object):
    def __init__(self, s = None):
        self.c = s
        self.children = {}
        self.isLeaf = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
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
    
    def searchNode(self, word):
        children = self.root.children
        for c in word:
            if c in children:
                t = children[c]
                children = t.children
            else:
                return None
        return t
    
    def search(self, word):
        t = self.searchNode(word)
        return bool(t and t.isLeaf)
    
    def startsWith(self, prefix):
        t = self.searchNode(prefix)
        return bool(t is not None)
    
    