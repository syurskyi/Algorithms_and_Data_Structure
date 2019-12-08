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



def checkwhetheritsabintree(root):
        if root == None:
                  return 1
        # false if left is > than root
        if root.l != None and root.l.v > root.v:
                  return 0

        # false if right is < than root
        if root.r != None and root.r.v < root.v:
                  return 0

        # false if, recursively, the left or right is not a BST
        if not checkwhetheritsabintree(root.l) or not checkwhetheritsabintree(root.r):
                  return 0

        # passing all that, it's a BST
        return 1


def levelOrder(root):
    items = []
    count=0
    items.insert(count,root)
    elements =""
    while items != []:
        temp = items.pop()
        elements= elements+str(temp.v)+ " "
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)
    print "Level order traversal of BST: "+ elements

def findsize(tree):
       if not tree:
          return 0
       return findsize(tree.l)+findsize(tree.r)+1

def printReverse(root):
    items = []
    count=0
    items.insert(count,root)
    elements =""
    while items != []:
        temp = items.pop()
        elements= str(temp.v)+ " " + elements
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)
    print "Level order traversal of BST: "+ elements


def maximumDepthOfTree(root):
        if root == None:
            return 0
        return max(maximumDepthOfTree(root.l), maximumDepthOfTree(root.r)) + 1


def deepestNode(root):
    items = []
    count=0
    items.insert(count,root)
    elements =""
    while items != []:
        temp = items.pop()
        elements= str(temp.v)+ " " + elements
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)
        for p in items: print p.v
        print "####"

    print "Deepest node is ",temp.v


def countLeaves(root):
    items = []
    count=0
    items.insert(count,root)
    elements =""
    while items != []:
        temp = items.pop()
        if temp.l is None and temp.r is None:
            count += 1
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)

    print "number of leafs in the tree ",count


def countFullNodes(root):
    items = []
    count=0
    items.insert(count,root)
    while items != []:
        temp = items.pop()
        if temp.l is not None and temp.r is not None:
            count += 1
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)

    print "number of full nodes in the tree ",count



def countHalfNodes(root):
    items = []
    count=0
    items.insert(count,root)
    while items != []:
        temp = items.pop()
        if (temp.l is None and temp.r is not None) or \
                        (temp.l is not None and temp.r is None):
            count += 1
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)

    print "number of half nodes in the tree ",count

ptr = 0
def diaTree(root):
        global ptr
        if(not root) :
                return 0
        left = diaTree(root.l);
        right = diaTree(root.r);

        if(left + right > ptr):
              ptr = left + right
        return max(left, right) + 1



def appendpath(root, path, paths):
        if not root:
                return 0

        path.append(root.v)
        print "PATH:",path
        paths.append(path)
        print "PATHS:",paths
        appendpath(root.l, path + [root.v], paths)
        appendpath(root.r, path + [root.v], paths)


def getthepathofeachnode(rootnode):
    nodepaths = []
    appendpath(rootnode, [], nodepaths)
    print 'path of nodes:', nodepaths


def getthepath(root, val, path, paths):
    
    
    print "root", root
    print "root.data", root.v
    print "val", val
    print "path", path
    print "paths", paths

    if not root:
        return False

    if not root.l and not root.r:
        if root.v == val:
            path.append(root.v)
            paths.append(path)
            return True
        else:
            return False

    left = getthepath(root.l, val - root.v, path + [root.v], paths)
    right = getthepath(root.r, val - root.v, path + [root.v], paths)
    return left or right


def checkwhetherpathhassum(root, val):
    paths = []
    getthepath(root, val, [], paths)
    print 'sum:', val
    print 'paths:', paths


def sumOfNodes(root):
    items = []
    count=0
    items.insert(count,root)
    sum=0
    while items != []:
        temp = items.pop()
        sum += temp.v 
        if temp.l!=None:
            items.insert(0,temp.l)
        if temp.r!=None:
            items.insert(0,temp.r)
        for p in items: print p.v
        print "####"

    print "Total sum of all nodes is ",sum



#     3
# 0     4
#   2      8
tree = binTree()
tree.addnode(3)
tree.addnode(4)
tree.addnode(0)
tree.addnode(-1)
tree.addnode(8)
tree.addnode(2)
tree.addnode(3.5)
tree.printFullTree()
print "The sizeof the tree is:"
print(findsize(tree.root))
