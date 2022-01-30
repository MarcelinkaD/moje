def maint():
    odleglosc_przyjaciela = int(input())
    aktualny_krok = 5
    wynik = 0
    
    while(odleglosc_przyjaciela != 0):
        if(odleglosc_przyjaciela // aktualny_krok != 0):
            wynik += odleglosc_przyjaciela // aktualny_krok
            odleglosc_przyjaciela -= (odleglosc_przyjaciela // aktualny_krok) * aktualny_krok
        else:
            aktualny_krok -= 1
            
    print(wynik)
    
maint()