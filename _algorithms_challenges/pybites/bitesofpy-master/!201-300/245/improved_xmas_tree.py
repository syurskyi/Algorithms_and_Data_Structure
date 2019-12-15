STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description"""
    width = rows * 2 - 1
    out = [f'{STAR:^{width}}']
    for n in range(rows):
        out.append(f'{LEAF * (n * 2 + 1):^{width}}')
    trunk = TRUNK * (rows + (1 if rows % 2 == 0 else 0))
    out.append(f'{trunk:^{width}}')
    out.append(f'{trunk:^{width}}')
    return '\n'.join(out)
