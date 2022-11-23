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

        __ node __ N..
            node _ Node(c)

        __ c < ?.character:
            ?.leftNode _ putItem(?.leftNode, key, value, index)
        ____ c > ?.character:
            ?.rightNode _ putItem(?.rightNode, key, value, index)
        ____ index < l..(key) - 1:
            ?.middleNode _ putItem(?.middleNode, key, value, index + 1)
        ____
            ?.value _ value

        r_ node;

    ___ get key

        node _ getItem(rootNode, key, 0)

        __ node __ N..
            r_ -1

        r_ ?.value

    ___ getItem node, key, index

        __ node __ N..
            r_ N..

        c _ key[index]

        __ c < ?.character:
            r_ getItem(?.leftNode, key, index)
        ____ c > ?.character:
            r_ getItem(?.rightNode, key, index)
        ____ index < l..(key) - 1:
            r_ getItem(?.middleNode, key, index + 1)
        ____
            r_ node


__ __name__ __ "__main__":
    tst _ TST()

    tst.put("apple", 100)
    tst.put("orange", 200)

    print(tst.get("orange"))
