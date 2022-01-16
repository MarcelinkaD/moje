# https://szkopul.edu.pl/c/mistrz-programowania-2022/p/rek
def main():
    liczba_ekranow, liczba_wlascicieli, budzet = map(int, input().split())
    ekrany = list(map(int, input().split()))
    oferty = list(map(int, input().split()))
    glowa = 0
    ogon = 0
    kupieni = [0] * liczba_wlascicieli
    oferty.insert(0, 0)
    kupieni.insert(0, 0)
    aktualny_budzet = 0
    wynik = 0
    
    
    while (ogon < liczba_ekranow):
        while (glowa < liczba_ekranow) and (aktualny_budzet <= budzet):
            if(kupieni[ekrany[glowa]] == 0):
                aktualny_budzet += oferty[ekrany[glowa]]
                kupieni[ekrany[glowa]] += 1
                glowa += 1
            else:
                kupieni[ekrany[glowa]] += 1
                glowa += 1
            if(aktualny_budzet <= budzet):
                wynik = max(glowa - ogon, wynik)
                
        kupieni[ekrany[ogon]] -= 1
        if(kupieni[ekrany[ogon]] == 0):
            aktualny_budzet -= oferty[ekrany[ogon]]
        ogon += 1
        
    print(wynik)
        
main()