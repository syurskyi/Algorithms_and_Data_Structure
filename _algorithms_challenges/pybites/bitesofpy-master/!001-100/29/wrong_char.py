# def get_index_different_char(chars):
#     char_vals = [(1 if str(c).isalnum() else 0) for c in chars]
#     return char_vals.index(1 if sum(char_vals) == 1 else 0)

def get_index_different_char(chars):
    '''
    This algorithm finishes early. It does not definitely traverse the whole list.
    To do this I tally how many alphanumeric and non alphanumeric characters I
    see as i iterate the list. It can be inferred (I assume) from the specification of the
    problem that if I count 2 of one type I know the majority and can exit
    as soon as I have come across a minority type.
    '''
    an = {False: 0, True: 0}  # alphanumeric counter
    p = 0  # tracks alphanumericity (I'm sure this is not a word) of the first character
    for ch in chars:
        c = str(ch).isalnum()  # the defacto test
        # In the case when the odd character is in the first 2 characters, the 'p'
        # variable allows me to determine the initial characters type and locate the
        # position of the minority type within the first 2 characters.
        if an[False] == 1 == an[True]:
            return 1 - p if c else p
        an[c] += 1
        if (c and an[False] < 2) or (not c and an[True] < 2):
            if c and sum(an) == 0:
                p = 1
            continue
        return chars.index(ch)
