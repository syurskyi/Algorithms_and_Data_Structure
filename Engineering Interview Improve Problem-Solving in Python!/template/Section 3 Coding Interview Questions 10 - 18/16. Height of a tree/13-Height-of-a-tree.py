import BST


tree = BST.BST(10)
tree.insert(5, tree.root)
tree.insert(15, tree.root)
tree.insert(25, tree.root)
tree.insert(12, tree.root)
tree.insert(35, tree.root)
print(tree.height(tree.root))