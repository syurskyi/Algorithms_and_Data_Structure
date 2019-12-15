def evenodd():
    n = int(input("Type an integer here: "))
    if n % 2 == 0:
        return f"Your number, {n}, is an even number."
    return f"Your number, {n}, is an odd number."
print(evenodd())
print(evenodd())