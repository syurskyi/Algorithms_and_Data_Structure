
def RockPaperScissors():
    """
    Rock Paper Scissors
    In Turkish(Türkçesi): Taş kağat makas oyunu
    """
    print("Taş Kağıt Makas. Birini seç")
    _PlayAgain()
    
def _CheckTheWin(p1: str, p2: str):
    TKM = {"taş": 1, "kağıt": 2, "makas": 3} # taş, kağıt, makas
    KazanmaSarti = ((-1,2),(-2,1)) # taş, kağıt, makas değerlerinin arasındaki farktan geliyor.
    ilksecim = TKM[p1]
    ikincisecim = TKM[p2]
    fark = ilksecim - ikincisecim
    if fark in KazanmaSarti[0]:
        print("İlk oyuncu oyuncu kazandı.")
        return "ilk" # iyi değil ama şimdilik idare eder.
    elif fark in KazanmaSarti[1]:
        print("İkinci oyuncu ikinci oyuncu kazandı.")
        return "ikinci" # iyi değil ama şimdilik idare eder.
    else:
        print("beraberlik")

def _PlayAgain():
    devammı = lambda cevap: str(input("Tekrardan oynamak ister misiniz? Evet(E)/Hayır(H)")).lower() in (cevap)
    while True:
      p1 = str(input("İlk Oyuncu: ")).strip().lower()
      p2 = str(input("İkinci Oyuncu: ")).strip().lower()
      _CheckTheWin(p1,p2)
      if devammı("evet"): continue # tekrar oynadığında sonuç tekrar gözükmeli
      else: print("Oyun bitti."); break