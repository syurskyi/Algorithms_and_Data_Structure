
def palindrome():
    """ 
    palindrome: hem soldan hem sağdan okunuşu aynı olan kelime yada veri kümesidir.
    """
    pal=str(input("palindrome kelime mi?"))
    check_palindrome = lambda pal: pal == pal[::-1]
    if check_palindrome(pal):
        print("palindrome kelimedir")
    else:
        print("palindrome kelime değildir.")