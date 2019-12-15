import random
def ListComprehensions():
    test1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) # programın girdisi
    listlenght= 10
    test2 = (random.randint(3,17) for _ in range(listlenght))
    CiftSayi= list(number for number in test2 if not number%2)
    print(CiftSayi)
    return CiftSayi