#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.l = None
        self.r = None
        self.v = data

class binTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addnode(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if(data < node.v):
            if(node.l != None):
                self._add(data, node.l)
            else:
                node.l = Node(data)
        else:
            if(node.r != None):
                self._add(data, node.r)
            else:
                node.r = Node(data)

    def findnode(self, data):
        if(self.root != None):
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if(data == node.v):
            return node
        elif(data < node.v and node.l != None):
            self._find(data, node.l)
        elif(data > node.v and node.r != None):
            self._find(data, node.r)

    def deleteTree(self):
        self.root = None

    def printFullTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)


def maxNodeLoop(root):
   if not root:
      return 0
   while root.r != None:
         root=root.r
   print root.v 
        


#     3
# 0     4
#   2      8
tree = binTree()
tree.addnode(3)
tree.addnode(4)
tree.addnode(0)
tree.addnode(8)
tree.addnode(2)
tree.printFullTree()
print "max value is:"
maxNodeLoop(tree.root)
