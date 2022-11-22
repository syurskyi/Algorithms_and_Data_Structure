
c_ Stack:

    ? ? - 
        stack _ []

    # O(1) running time
    ? ? is_empty
        r_ stack __ []

    # O(1) running time
    ? ? push data
        stack.append(data)

    # O(1) because we manipulate the last item
    ? ? pop

        __ size_stack < 1:
            r_ N..

        data _ stack[-1]
        del stack[-1]
        r_ data

    # O(1) constant running time
    ? ? peek
        r_ stack[-1]

    # O(1)
    ? ? size_stack
        r_ l..(stack)
