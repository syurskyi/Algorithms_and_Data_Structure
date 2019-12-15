def transform(lst):
    output= []
    for i in lst:
        if i % 2 == 0:
            output.append(i-1)
        else:
             output.append(i+1)
    return output
