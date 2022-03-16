from sys import stdin
input = stdin.readline

def gasienica(tab, dlugosc_tab, do_kradziezy):
    ogon = -1
    glowa = -1
    wynik_najlepszy = dlugosc_tab + 1
    akt_wynik = 0

    while (ogon < dlugosc_tab - 1):
        while (glowa < dlugosc_tab - 1) and (akt_wynik <= do_kradziezy):
            glowa += 1
            akt_wynik += tab[glowa]
            
            if(akt_wynik == do_kradziezy):
                wynik_najlepszy = min(glowa - ogon, wynik_najlepszy)
        
        ogon += 1
        akt_wynik -= tab[ogon]
    
        if(akt_wynik == do_kradziezy):
            wynik_najlepszy = min(glowa - ogon, wynik_najlepszy)
        
    
    return wynik_najlepszy
    
def main():
    liczba_grzadek, liczba_do_zabrania = map(int, input().split())
    grzadki = list(map(int, input().split()))
    wynik = 0
    
    if liczba_do_zabrania in grzadki:
        return "1"
    else:
        wynik = int(gasienica(grzadki, liczba_grzadek, liczba_do_zabrania))
        
    if wynik == liczba_grzadek + 1:
        return "Nie"
    else:
        return wynik
    
print(main())