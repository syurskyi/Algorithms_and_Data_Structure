____ queuelinked _______ LinkedQueue


c_ BinaryTree:

    c_ _Node:

        __slots__ _ '_element', '_left', '_right'

        ___ -(self, element, left_None, right_None):
            _element _ element
            _left _ left
            _right _ right

    ___ -
         root _ None
        _size _ 0

    ___ maketree(self, e, left, right):
        _root _ _Node(e, left._root, right._root)
        left._root _ None
        right._root _ None

    ___ levelorder
        Q _ LinkedQueue()
        t _ _root
        print(t._element, end_'--')
        Q.enqueue(t)

        while not Q.is_empty():
            t _ Q.dequeue()
            __ t._left:
                print(t._left._element, end_'--')
                Q.enqueue(t._left)
            __ t._right:
                print(t._right._element, end_'--')
                Q.enqueue(t._right)

    ___ inorder(self, troot):
        __ troot:
            inorder(troot._left)
            print(troot._element, end_'--')
            inorder(troot._right)

    ___ preorder(self,troot):
        __ troot:
            print(troot._element,end_'--')
            preorder(troot._left)
            preorder(troot._right)

    ___ postorder(self, troot):
        __ troot:
            postorder(troot._left)
            postorder(troot._right)
            print(troot._element, end_'--')


a _ BinaryTree()
x _ BinaryTree()
y _ BinaryTree()
z _ BinaryTree()
r _ BinaryTree()
s _ BinaryTree()
t _ BinaryTree()

x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20, x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)

t.levelorder()
print()
t.preorder(t._root)
print()
t.inorder(t._root)
print()
t.postorder(t._root)
print()
