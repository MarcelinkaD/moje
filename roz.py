from sys import stdin
input = stdin.readline

def main():
    liczba_liczb, roznica = map(int, input().split())
    liczby = list(map(int, input().split()))
    ogon = 0
    glowa = -1
    wynik_najlepszy = 0
    akt_wynik = 0
    liczby.sort()
    
    while (ogon < liczba_liczb - 1):
        while (glowa < liczba_liczb - 1) and (akt_wynik <= roznica):
            glowa += 1
            
            akt_wynik = liczby[glowa] - liczby[ogon]
            
            if(akt_wynik <= roznica):
                wynik_najlepszy = max(glowa - ogon + 1, wynik_najlepszy)
        
        ogon += 1
        akt_wynik = liczby[glowa] - liczby[ogon]
        
        if(akt_wynik <= roznica):
            wynik_najlepszy = max(glowa - ogon + 1, wynik_najlepszy)
    
    print(wynik_najlepszy)
    
main()