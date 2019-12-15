def char_index(word, char):
    output = []
    for i in range(len(word)):
        if word[i] == char:
            output.append(i)
        elif char not in word:
            return None
    output.sort()
    if len(output) == 1:
        output.append(output[0])
    if len(output) > 2:
        for i in range(1,len(output)- 1):
            output.pop(i)
    return output
