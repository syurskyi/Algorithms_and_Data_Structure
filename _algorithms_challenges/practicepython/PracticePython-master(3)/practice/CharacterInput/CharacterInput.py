import datetime
def CharacterInputSol():
    isim = input("Adın nedir?: ")
    try:
        yas = int(input("Kaç yaşındasın?: "))
    except ValueError:
        print("sayısal değer girilmedi.")
    CurrentYear = datetime.date.today().year
    HangiYıl = str((CurrentYear - yas)+100)
    print("%s %s yılında 100 yaşında olacak."% (isim, HangiYıl))
