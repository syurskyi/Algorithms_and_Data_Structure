def increment_to_top(lst):
    sl = sorted(lst)
    output = 0
    index = 0
    while index < (len(sl) - 1):
         output += sl[-1] - sl[index]
         index += 1
    return output
