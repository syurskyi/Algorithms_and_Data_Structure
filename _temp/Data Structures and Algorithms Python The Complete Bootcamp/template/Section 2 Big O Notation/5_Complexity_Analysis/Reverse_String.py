# 1.1) Python Reverse String using Slicing

___ reverse_slicing(s
    r_ s[::-1]

input_str _ 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))


# 1.2) Reverse String using For Loop

___ reverse_for_loop(s
    s1 _ ''
    ___ c __ s:
        s1 _ c + s1  # appending chars in reverse order
    r_ s1

input_str _ 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))


# 1.3) Reverse a String using While Loop

___ reverse_while_loop(s
    s1 _ ''
    length _ l..(s) - 1
    _____ length >_ 0:
        s1 _ s1 + s[length]
        length _ length - 1
    r_ s1

input_str _ 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))


# 1.4) Reverse a String using join() and reversed()

___ reverse_join_reversed_iter(s
    s1 _ ''.j..(r..(s))
    r_ s1

# 1.5) Python Reverse String using List reverse()

___ reverse_list(s
    temp_list _ list(s)
    temp_list.reverse()
    r_ ''.j..(temp_list)

# 1.6) Python Reverse String using Recursion

___ reverse_recursion(s
    __ l..(s) __ 0:
        r_ s
    ____
        r_ reverse_recursion(s[1:]) + s[0]