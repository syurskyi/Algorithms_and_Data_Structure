INDENTS = 4


def print_hanging_indents(poem):
    indent = False
    for line in poem.splitlines():
        l = line.strip()
        if len(l) == 0:
            indent = False
            continue
        if indent:
            print(f'{" " * INDENTS}{l}')
        else:
            print(f'{l}')
            indent = True
