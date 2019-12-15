def XO(txt):
    s = txt.lower()
    if s.count("x") == 0 and s.count("o") == 0:
        return True
    elif s.count("x") == s.count("o"):
        return True
    else:
        return False
