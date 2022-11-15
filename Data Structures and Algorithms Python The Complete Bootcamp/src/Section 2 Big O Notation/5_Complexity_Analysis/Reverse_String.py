# 1.1) Python Reverse String using Slicing

def reverse_slicing(s):
    return s[::-1]

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using slicing =', reverse_slicing(input_str))


# 1.2) Reverse String using For Loop

def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using for loop =', reverse_for_loop(input_str))


# 1.3) Reverse a String using While Loop

def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

input_str = 'ABç∂EF'

if __name__ == "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))


# 1.4) Reverse a String using join() and reversed()

def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1

# 1.5) Python Reverse String using List reverse()

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

# 1.6) Python Reverse String using Recursion

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]