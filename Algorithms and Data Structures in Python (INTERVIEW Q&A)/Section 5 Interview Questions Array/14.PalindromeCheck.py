
# it has O(s) so basically linear running time complexity as far as the number
# of letters in the string is concerned
def is_palindrome(s):

    original_string = s
    # this is what we have implemented in the previous lecture in O(N)
    reversed_string = reverse(s)

    if original_string == reversed_string:
        return True

    return False


# O(N) linear running time where N is the number of letters in string s N=len(s)
def reverse(data):

    # string into a list of characters
    data = list(data)

    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(data)-1

    while end_index > start_index:
        # keep swapping the items

        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    # transform the list of letters into a string
    return ''.join(data)


if __name__ == '__main__':
    print(is_palindrome('Kevin'))
