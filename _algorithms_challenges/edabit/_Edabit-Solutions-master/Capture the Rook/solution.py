def can_capture(rooks):
    s1 = rooks[0][0]
    s2= rooks[1][0]
    e1 = rooks[0][1]
    e2 = rooks[1][1]
    if s1 == s2 or e1 == e2:
        return True
    else:
        return False
