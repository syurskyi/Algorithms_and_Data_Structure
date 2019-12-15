def same_ascii(a, b):
    s1 = 0
    s2 = 0
    for i in a:
      s1 +=  ord(i)
    for i in b:
        s2 += ord(i)
    if s1 == s2:
        return True
    else:
        return False
