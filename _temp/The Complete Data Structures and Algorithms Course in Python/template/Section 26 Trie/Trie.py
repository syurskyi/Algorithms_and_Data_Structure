#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ TrieNode:
    ___ -  
        children _     # dict
        endOfString _ F..

c_ Trie:
    ___ -  
        root _ TrieNode()
    
    ___ insertString word
        current _ root
        ___ i __ word:
            ch _ i
            node _ current.children.get(ch)
            __ node __ N..
                node _ TrieNode()
                current.children.update({ch:node})
            current _ node
        current.endOfString _ T..
        print("Successfully inserted")
    
    ___ searchString word
        currentNode _ root
        ___ i __ word:
            node _ ?.children.get(i)
            __ node __ N..
                r_ F..
            currentNode _ node

        __ ?.endOfString __ T..:
            r_ T..
        ____
            r_ F..
        

___ deleteString(root, word, index
    ch _ word[index]
    currentNode _ root.children.get(ch)
    canThisNodeBeDeleted _ F..

    __ l..(?.children) > 1:
        deleteString(currentNode, word, index+1)
        r_ F..
    
    __ index __ l..(word) - 1:
        __ l..(?.children) >_ 1:
            ?.endOfString _ F..
            r_ F..
        ____
            root.children.p.. ch)
            r_ T..
    
    __ ?.endOfString __ T..:
        deleteString(currentNode, word, index+1)
        r_ F..

    canThisNodeBeDeleted _ deleteString(currentNode, word, index+1)
    __ canThisNodeBeDeleted __ T..:
        root.children.p.. ch)
        r_ T..
    ____
        r_ F..



    
newTrie _ Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))