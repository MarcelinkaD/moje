from sys import stdin
input = stdin.readline

def main():
    liczba_domow, dol, gura = map(int, input().split())
    domy = list(map(int, input().split()))
    domy.insert(0, 0)
    literki = input().strip()
    
    maks_skok_gura = [0] * (liczba_domow + 1)
    maks_skok_dol = [0] * (liczba_domow + 1)
    

    ogon = liczba_domow
    glowa = liczba_domow

    while (ogon > 0):
        while (glowa > 0) and (domy[glowa] - domy[ogon] <= gura):
            glowa -= 1
        
        maks_skok_gura[ogon] = glowa + 1
        ogon -= 1
        

    ogon = 1
    glowa = 1
    
    while (ogon < liczba_domow + 1):
        while (glowa < liczba_domow + 1) and (domy[ogon] - domy[glowa] <= dol):
            glowa += 1
        
        maks_skok_dol[ogon] = glowa - 1
        ogon += 1        


    akt_pozycja = 1
    maks_skok = 0
    
    for i in range(len(literki)):
        literka = literki[i]
        if literka == "g":
            maks_skok = max(maks_skok, akt_pozycja - maks_skok_gura[akt_pozycja] )
            akt_pozycja = maks_skok_gura[akt_pozycja]
        else:
            maks_skok = max(maks_skok, maks_skok_dol[akt_pozycja] - akt_pozycja )
            akt_pozycja = maks_skok_dol[akt_pozycja]
        
        

    print(str(akt_pozycja) + " " + str(maks_skok))


main()