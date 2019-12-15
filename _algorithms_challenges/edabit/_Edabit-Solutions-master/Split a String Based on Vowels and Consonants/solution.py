def split(txt):
    output = ""
    output2 = ""
    vset = {"a","e","i","o","u"}
    for i in txt:
        if i in vset:
            output += i
        if i not in vset:
            output2 += i
    return output + output2
