def hash_plus_count(txt):
    if txt == "":
        return [0,0]
    index = 0
    output =[]
    check = ["#","+"]
    while index < len(check):
        a = txt.count(check[index])
        output.append(a)
        index = index + 1
    return output
