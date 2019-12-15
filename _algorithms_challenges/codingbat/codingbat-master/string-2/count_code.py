''' Return the number of times that the string "code" appears anywhere in the
given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
count. '''


def count_code(str):
    code_count = 0
    for i, _ in enumerate(str):
        if str[i:i + 2] == 'co' and str[i + 3:i + 4] == 'e':
            code_count += 1
    return code_count
