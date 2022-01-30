def main():
    liczba_stacji, odleglosc, pojemnosc_baku = map(int, input().split())
    stacje = list(map(int, input().split()))
    przejechane_stacje = 0            
    licznik = 0
    aktualny_bak = 0
    przejechane_kilometry = 0
    
    while licznik < liczba_stacji and aktualny_bak >= 0:
        if stacje[licznik] >= pojemnosc_baku:
            aktualny_bak = pojemnosc_baku
            przejechane_stacje += 1
        else:
            aktualny_bak += stacje[licznik]
            przejechane_stacje += 1
        
        if(aktualny_bak - odleglosc < 0):
            przejechane_kilometry += aktualny_bak
            break
        else:
            if(przejechane_stacje == liczba_stacji):
                przejechane_kilometry += aktualny_bak
                licznik += 1
            else:
                aktualny_bak -= odleglosc
                przejechane_kilometry += odleglosc
                licznik += 1
            
            
        
    
    print(str(przejechane_stacje) + " " + str(przejechane_kilometry))
    
main()