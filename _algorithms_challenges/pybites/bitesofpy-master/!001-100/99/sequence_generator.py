from string import ascii_uppercase


def sequence_generator():
    while True:
        for a in enumerate(ascii_uppercase, start=1):
            yield a[0]
            yield a[1]
