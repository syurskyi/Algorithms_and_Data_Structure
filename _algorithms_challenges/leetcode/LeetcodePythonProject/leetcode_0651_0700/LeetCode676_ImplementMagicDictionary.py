'''
Created on Oct 18, 2017

@author: MT
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isLeaf = False

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.root = TreeNode(None)
        for word in dict:
            node = self.root
            for c in word:
                if c not in node.children:
                    newNode = TreeNode(c)
                    node.children[c] = newNode
                node = node.children[c]
            node.isLeaf = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root, word, 0, False)
    
    def helper(self, node, word, ind, diffFlag):
        if not node: return False
        if ind == len(word):
            if node.isLeaf and diffFlag:
                return True
            return False
        c = word[ind]
        for c0 in node.children:
            if c0 != c and diffFlag:
                continue
            if self.helper(node.children.get(c, None), word, ind+1, diffFlag) or\
                (c0 != c and self.helper(node.children[c0], word, ind+1, True)):
                return True
        return False

if __name__ == '__main__':
    magicDict = MagicDictionary()
    magicDict.buildDict(['hello', 'leetcode', 'hallo'])
    print(magicDict.search('hello'))
    print(magicDict.search('hhllo'))
    print(magicDict.search('hell'))
    print(magicDict.search('leetcoded'))
