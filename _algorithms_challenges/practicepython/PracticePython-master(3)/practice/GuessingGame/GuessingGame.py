import random
def GuessingGame():
    tahminedilece = random.randint(1,9)
    tahmin = 0
    kactahmin = 0
    while tahmin != tahminedilece and tahmin != "exit":
        tahmin = input("Enter a tahmin between 1 to 9: ")
        if tahmin == "exit":
            break
        tahmin = int(tahmin)
        kactahmin += 1
        if tahmin < tahminedilece:
            print("az oldu yukarı")
        elif tahmin > tahminedilece:
            print("çok oldu aşağı")
        else:
            print("İşte bu :)")
            print("Sadece", kactahmin, "denemede yaptın.")
