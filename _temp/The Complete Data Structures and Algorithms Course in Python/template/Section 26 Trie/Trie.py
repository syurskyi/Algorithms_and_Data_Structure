#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

c_ TrieNode:
    ___ -  
        children _ {}
        endOfString _ False

c_ Trie:
    ___ -  
        root _ TrieNode()
    
    ___ insertString word
        current _ root
        ___ i __ word:
            ch _ i
            node _ current.children.get(ch)
            __ node == N..:
                node _ TrieNode()
                current.children.update({ch:node})
            current _ node
        current.endOfString _ True
        print("Successfully inserted")
    
    ___ searchString word
        currentNode _ root
        ___ i __ word:
            node _ currentNode.children.get(i)
            __ node == N..:
                r_ False
            currentNode _ node

        __ currentNode.endOfString == True:
            r_ True
        ____
            r_ False
        

___ deleteString(root, word, index
    ch _ word[index]
    currentNode _ root.children.get(ch)
    canThisNodeBeDeleted _ False

    __ len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        r_ False
    
    __ index == len(word) - 1:
        __ len(currentNode.children) >_ 1:
            currentNode.endOfString _ False
            r_ False
        ____
            root.children.pop(ch)
            r_ True
    
    __ currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        r_ False

    canThisNodeBeDeleted _ deleteString(currentNode, word, index+1)
    __ canThisNodeBeDeleted == True:
        root.children.pop(ch)
        r_ True
    ____
        r_ False



    
newTrie _ Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))