def is_symmetrical(num):
    b_str =  str(num)
    a_str = str(num)
    if a_str[::-1] == b_str:
        return True
    else:
        return False
