import string

""""
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics) """

def get_index_different_char(chars):
    alphanumeric = list(string.ascii_letters + string.digits)
    alp = [chars.index(i) for i in chars if i not in alphanumeric]
    nonalp = [chars.index(i) for i in chars if i in alphanumeric]
    return int(alp[0]) if len(alp) == 1 else int(nonalp[0])


chars = ['.', '{', ' ^', '%', 'a']
get_index_different_char(chars)
