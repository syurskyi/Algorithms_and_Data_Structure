import math
def PrimalityFunctions():
    try:
        sayı = int(input("Lütfen bir sayı girin: " + "\n" + ">>>"))
    except ValueError:
        print("lütfen sayı girin.")
    sayı = int(sayı)
    prime = False
    if sayı > 0:
        for x in range (3, sayı - 1, 2): # 2 ile denemye gerek yok ve çift sayılar zaten asal olamaz. En iyi yolu asallarla test etmek gerek.
            if math.sqrt(sayı) > x or sayı % x != 0: # sayı bölünmediyse yenisiyle test et.
                continue 
            elif sayı % x == 0: # bölünürse asal değil.
                print("asal değildir.")
                return("asal değil.")
        print("asaldır.") # sayı wasn't evenly divisible by any x, so it's prime
    elif sayı == 2:
        print("asaldır.")
        return("asaldır.") # 2 asal sayıdır.
    elif sayı == 0:
        print("asal değildir.")
        return("asal değil.") # sıfır asal değildir.
    else: # sıfırdan küçükler asal değildir.
        print("asal değildir.")
        return("asal değil.")