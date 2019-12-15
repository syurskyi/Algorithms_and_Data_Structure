def add_ending(lst, ending):
    index = 0
    output = []
    while index <len(lst):
      s = lst[index] + ending
      output.append(s)
      index += 1
    return output
