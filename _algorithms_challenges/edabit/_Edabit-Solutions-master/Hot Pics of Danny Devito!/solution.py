def prevent_distractions(txt):
    a_list = ["Danny Devito","roasts","vine","meme","anime"]
    index = 0
    while index < len(a_list):
        word = a_list[index]
        if txt.count(word) > 0:
            return "NO!"
        index = index + 1
    return "Safe watching!
