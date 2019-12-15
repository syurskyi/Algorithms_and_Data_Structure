
def Divisors():
    try:
        num=int(input("Bölmek istediğiniz sayı nedir?").strip())
    except ValueError:
        print("sorun var.")
    AllOfNumbers = list(range(1,num+1))
    divisorList = list(number for number in AllOfNumbers if not num %number)
    
    print(divisorList)
    return divisorList  
