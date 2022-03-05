from sys import stdin
input = stdin.readline

def main():
    ilosc_liczb = int(input())
    liczby = []
    glowa = -1
    ogon = 0
    wynik_najlepszy = 0
    
    for i in range(ilosc_liczb):
        ik = int(input())
        liczby.append(ik)
        
    liczby.sort()
    
    while (ogon < ilosc_liczb - 1):
        while (glowa < ilosc_liczb - 1) and (liczby[ogon] + liczby[ogon + 1] > liczby[glowa + 1]):
            glowa += 1
            wynik_najlepszy = max(glowa - ogon + 1, wynik_najlepszy)
         
        ogon += 1
        
        
    print(wynik_najlepszy)     
    
    
main()