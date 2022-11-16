c_ Node o..

    ___ -  character
        character _ character
        leftNode _ N..
        middleNode _ N..
        rightNode _ N..
        value _ 0


c_ TST o..

    ___ -  
        rootNode _ N..

    ___ put key, value
        rootNode _ putItem(rootNode, key, value, 0)

    ___ putItem node, key, value, index

        c _ key[index]

        __ node == N..:
            node _ Node(c)

        __ c < node.character:
            node.leftNode _ putItem(node.leftNode, key, value, index)
        elif c > node.character:
            node.rightNode _ putItem(node.rightNode, key, value, index)
        elif index < len(key) - 1:
            node.middleNode _ putItem(node.middleNode, key, value, index + 1)
        ____
            node.value _ value

        r_ node;

    ___ get key

        node _ getItem(rootNode, key, 0)

        __ node == N..:
            r_ -1

        r_ node.value

    ___ getItem node, key, index

        __ node == N..:
            r_ N..

        c _ key[index]

        __ c < node.character:
            r_ getItem(node.leftNode, key, index)
        elif c > node.character:
            r_ getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            r_ getItem(node.middleNode, key, index + 1)
        ____
            r_ node


__ __name__ == "__main__":
    tst _ TST()

    tst.put("apple", 100)
    tst.put("orange", 200)

    print(tst.get("orange"))
