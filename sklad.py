from sys import stdin
input = stdin.readline

def gasenica(tablica, len, zapotrzebowanie_cementu):
    ogon = -1
    glowa = -1
    wynik_super = len + 1
    akt_wwyynniikk = 0
    
    while ogon < len - 1:
        while glowa < len - 1 and akt_wwyynniikk <= zapotrzebowanie_cementu:
            glowa += 1
            akt_wwyynniikk += tablica[glowa]
            
            if akt_wwyynniikk == zapotrzebowanie_cementu:
                wynik_super = min(glowa - ogon, wynik_super)
            
        ogon += 1
        akt_wwyynniikk -= tablica[ogon]       
        
        if akt_wwyynniikk == zapotrzebowanie_cementu:
            wynik_super = min(glowa - ogon, wynik_super)
            
    return wynik_super
    
def main():
    liczba_wagonow, suma = map(int, input().split())
    wagony = list(map(int, input().split()))
    wynik = 0 
    
    if suma in wagony:
        return 1
    else:
        wynik = int(gasenica(wagony, liczba_wagonow, suma))
        
    if wynik == liczba_wagonow + 1:
        return "N"
    else:
        return wynik
    
print(main())