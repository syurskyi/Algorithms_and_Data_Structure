def anagram(s,t):
    
    s = s.lower().replace(' ','')
    t = t.lower().replace(' ','')
    if len(s) != len(t):
        return False
    for i in t:
        if i in s:
            continue
        return False

    return True