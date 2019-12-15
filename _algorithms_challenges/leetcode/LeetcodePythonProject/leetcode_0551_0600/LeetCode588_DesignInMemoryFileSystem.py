'''
Created on Sep 4, 2017

@author: MT
'''
class TreeNode(object):
    def __init__(self, folder=None):
        self.folder = folder
        self.content = ''
        self.children = {}
        self.childFolders = []
        self.isFile = False

class FileSystem(object):
    def __init__(self):
        self.root = TreeNode()
    
    def ls(self, path):
        path = path[1:]
        arr = path.split('/')
        if arr[0] == '':
            arr = []
        node = self.root
        for folder in arr:
            node = node.children[folder]
        node.childFolders.sort()
        if node.isFile:
            return [node.folder]
        else:
            return node.childFolders
    
    def mkdir(self, path):
        path = path[1:]
        arr = path.split('/')
        node = self.root
        for folder in arr:
            if folder in node.children:
                node = node.children[folder]
            else:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.append(folder)
                node = newNode
    
    def addContentToFile(self, filePath, content):
        filePath = filePath[1:]
        arr = filePath.split('/')
        file = arr[-1]
        arr = arr[:-1]
        node = self.root
        for folder in arr:
            if folder in node.children:
                node = node.children[folder]
            else:
                newNode = TreeNode(folder)
                node.children[folder] = newNode
                node.childFolders.append(folder)
                node = newNode
        if file in node.children:
            node.children[file].content += content
        else:
            newNode = TreeNode(file)
            node.children[file] = newNode
            node.childFolders.append(file)
            newNode.isFile = True
            newNode.content += content
    
    def readContentFromFile(self, filePath):
        filePath = filePath[1:]
        arr = filePath.split('/')
        node = self.root
        for folder in arr:
            node = node.children[folder]
        return node.content
