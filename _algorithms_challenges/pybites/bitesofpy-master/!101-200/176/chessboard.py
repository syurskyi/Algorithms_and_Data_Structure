WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    s = f'{WHITE}{BLACK}' * (size//2)
    for n in range(size//2):
        print(s)
        print(s[::-1])
