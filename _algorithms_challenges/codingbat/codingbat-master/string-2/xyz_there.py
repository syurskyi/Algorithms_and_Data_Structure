''' Return True if the given string contains an appearance of "xyz" where the
xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz"
does not. '''


def xyz_there(str):
    xyz_match = False
    for i, _ in enumerate(str):
        if str[i:i + 3] == 'xyz' and str[i - 1] != '.':
            xyz_match = True
    return xyz_match
