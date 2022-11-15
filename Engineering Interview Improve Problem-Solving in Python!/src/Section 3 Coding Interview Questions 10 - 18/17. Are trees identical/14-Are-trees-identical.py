import BST


tree = BST.BST(10)
tree.insert(5, tree.root)
tree.insert(15, tree.root)
tree.insert(25, tree.root)
tree.insert(12, tree.root)
tree.insert(35, tree.root)

tree2 = BST.BST(10)
tree2.insert(5, tree2.root)
tree2.insert(15, tree2.root)
tree2.insert(25, tree2.root)
tree2.insert(12, tree2.root)
tree2.insert(35, tree2.root)

print(tree.is_identical(tree2.root))
