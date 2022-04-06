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
        
    return wynik
    
def main():
    liczba_pytan = int(input())
    
    for i in range(liczba_pytan):
        liczba_kulek = int(input())
        liczba_kolorow = liczba_kulek
        wynik = potegowanie(liczba_kulek, liczba_kolorow) - liczba_kulek
        print(wynik % 1000000007)
        
    
main()