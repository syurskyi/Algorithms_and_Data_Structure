# 1.1) Python Reverse String using Slicing

___ reverse_slicing(s):
    r_ s[::-1]

input_str = 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))


# 1.2) Reverse String using For Loop

___ reverse_for_loop(s):
    s1 = ''
    ___ c __ s:
        s1 = c + s1  # appending chars __ reverse order
    r_ s1

input_str = 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using ___ loop =', reverse_for_loop(input_str))


# 1.3) Reverse a String using While Loop

___ reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    ______ length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    r_ s1

input_str = 'ABç∂EF'

__ __name__ __ "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))


# 1.4) Reverse a String using join() and reversed()

___ reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    r_ s1

# 1.5) Python Reverse String using List reverse()

___ reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    r_ ''.join(temp_list)

# 1.6) Python Reverse String using Recursion

___ reverse_recursion(s):
    __ len(s) __ 0:
        r_ s
    ____
        r_ reverse_recursion(s[1:]) + s[0]