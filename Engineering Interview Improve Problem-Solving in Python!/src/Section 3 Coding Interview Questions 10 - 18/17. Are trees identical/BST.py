class Node:
    val = 0
    left = 0
    right = 0
    def __init__(self, val):
        self.val = val

class BST:
    
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val, node):
        if node.val < val:
            if node.right:
                #go right
                self.insert(val, node.right)
            else:
                node.right = Node(val) #insert
        elif val < node.val:
            if node.left:
                #go left
                self.insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            print(val, " Already in tree")

    def number_of_leaves(self, node):
        if node.left and node.right:
            return self.number_of_leaves(node.left) + self.number_of_leaves(node.right)
        elif node.left:
            return self.number_of_leaves(node.left)
        elif node.right:
            return self.number_of_leaves(node.right)
        else:
            #leave
            return 1
    
    def number_of_leaves_i(self):
        leaves = 0
        nodes = [self.root]
        while nodes:
            node = nodes[0]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if (not node.left) and (not node.right):
                leaves += 1
            del nodes[0]
        return leaves

    def height(self, node):
        if node.left and node.right:
            print(node.val, " Height of left ", self.height(node.left)," Hegiht of right ", self.height(node.right))
            return 1 + max(self.height(node.left), self.height(node.right))
        elif node.left:
            #print(node.val, self.height(node.left))
            return 1 + self.height(node.left)
        elif node.right:
            #print(node.val, self.height(node.right))
            return 1 + self.height(node.right)
        else:
            #print(node.val)
            return 1

    def is_identical(self, second_root):
        nodes1 = [self.root]
        nodes2 = [second_root]
        while nodes1 and nodes2:
            node = nodes1[0]
            node2 = nodes2[0]
            if node.val == node2.val:
                if node.left:
                    nodes1.append(node.left)
                if node.right:
                    nodes1.append(node.right)
                if node2.left:
                    nodes2.append(node2.left)
                if node2.right:
                    nodes2.append(node2.right)
            else:
                return False
            del nodes1[0]
            del nodes2[0]
        return len(nodes1) == len(nodes2)