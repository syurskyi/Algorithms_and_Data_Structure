def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    return '\n'.join(f'{" " * (rows - row - 1)}{"*" * (row * 2 + 1)}' for row in range(rows))
