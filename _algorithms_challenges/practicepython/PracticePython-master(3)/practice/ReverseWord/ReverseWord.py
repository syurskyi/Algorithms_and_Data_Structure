
def ReverseWord():
    kelime= "vektörize çözümler oldu mu? Yoğurtlar mayalandı mı?"
    sonuc=' '.join(kelime.split()[::-1])
    print(sonuc)
    return sonuc