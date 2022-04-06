from sys import stdin
input = stdin.readline

def potegowanie(ile, do_czego):
    wynik = 1
    pot = ile
    while do_czego > 0:
        if do_czego % 2 == 1:
            wynik = wynik * pot
        pot = pot * pot
        pot %= 1000000007
        do_czego = do_czego // 2
        
    return wynik % 1000000007

def main():
    liczba_zawodnikow = int(input())
    
    zawodnicy = [0] * liczba_zawodnikow
    wyniki = [0] * liczba_zawodnikow
    
    for i in range(liczba_zawodnikow):
        zawodnik = int(input())
        zawodnicy[i] = zawodnik
     
    zawodnicy.insert(0,0)
    wyniki.insert(0,0)
    
        
    for i in range(1,liczba_zawodnikow + 1):
        for j in range(i + 1, liczba_zawodnikow + 1):
            z2_z1 = pow(zawodnicy[j], zawodnicy[i],1000000007)
            z1_z2 = pow(zawodnicy[i], zawodnicy[j],1000000007)

            if z2_z1 > z1_z2:
                wyniki[i] += 2
            elif z2_z1 < z1_z2:
                wyniki[j] += 2
            else:
                wyniki[i] += 1
                wyniki[j] += 1
    
    max_liczba = 0
    pos = 0
    
    if liczba_zawodnikow == 1:
        print(1)
    else:
        for i in range(1, len(wyniki)):
            if wyniki[i] > max_liczba:
                max_liczba = wyniki[i]
                pos = i
                
        print(pos)
    
main()