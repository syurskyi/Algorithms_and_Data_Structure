def OddEven():
    try:
        num = int(input("Bana kontrol etmek üzere bir sayı ver: "))
    except ValueError:
        print("lütfen sayı giriniz.")

    try:
        check = int(input("böleceğim sayıyı ver: "))
    except ValueError:
        print("lütfen sayı giriniz.")

    if num % 4 == 0:
        print(num, "4 ile bölünür")
    elif num % 2 == 0:
        print(num, "çift sayı mı?")
    else:
        print(num, "tek sayı mı?")

    if num % check == 0:
        print(num, "eşit olarak böler", check)
    else:
        print(num, "eşit olarak bölmez", check)

    
