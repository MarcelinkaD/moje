ile_ludzi = int(input())

ludzie = list(map(int, input().split()))

szybkosci = list(map(int, input().split()))



def CzyUdaSieSpodkac(czas):
    maxPocz = 0
    minKoniec = 1e9
    for i in range(ile_ludzi):
        droga = czas * szybkosci[i] 
        poczatek = ludzie[i] - droga
        koniec = ludzie[i] + droga
        maxPocz = max(maxPocz, poczatek)
        minKoniec = min(minKoniec, koniec)
        
        if(maxPocz > minKoniec):
            return False
   
    return True 

def WyszukajCzasBinarnie(poczatek, koniec):
    while koniec - poczatek > 1e-7:
        srodek = float((koniec + poczatek) / 2)
        if(CzyUdaSieSpodkac(srodek) == True):
            koniec = srodek
        else:
            poczatek = srodek
    
    return poczatek


print(WyszukajCzasBinarnie(0, 1e9))

