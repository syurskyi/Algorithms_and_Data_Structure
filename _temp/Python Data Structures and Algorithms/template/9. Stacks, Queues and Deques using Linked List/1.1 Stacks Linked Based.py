____ e.. _______ E..


c_ LinkedStack:
    c_ _Node:
        __slots__ _ '_element' , '_next'

        ___ -(self, element, next):
            _element _ element
            _next _ next

    ___ -
        _head _ None
        _size _ 0

    ___ -l
        r_ _size

    ___ is_empty
        r_ _size __ 0

    ___ push e
        _head _ _Node(e, _head)
        _size _ _size + 1

    ___ pop
        __ ?
            r_ ? 'Stack is Empty'
        value _ _head._element
        _head _ _head._next
        _size _ _size - 1
        r_ value

    ___ top
        __ ?
            r_ ? 'Stack is Empty'
        r_ _head._element

    ___ display
        temp _ _head
        while temp:
            print(temp._element, end_'-->')
            temp _ temp._next
        print()


ls _ LinkedStack()
ls.push(10)
ls.push(20)

ls.push(30)
ls.push(40)
ls. display()
print('Popped: ', ls.pop())
ls. display()
ls.push(70)
ls.display()
print('Top Element: ', ls.top())
print('Popped: ', ls.pop())
ls.display()
