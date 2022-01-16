def main():
    MAXN = int(1e5 + 7)
    sito = [0] * MAXN
    sito[1] = 1
    liczba_zapytan = int(input())
    
    for i in range(2, MAXN):
        if sito[i] == 0:
            sito[i] = i
            for k in range(i, MAXN, i):
                sito[k] = i
                
    for i in range(liczba_zapytan):
        liczba_liczb = int(input())
        dzielniki = {}
        liczby = list(map(int, input().split()))

        for m in liczby:
            dzielniki[sito[m]] = dzielniki.get(sito[m], 0) + 1
            
        najwiekszyDzielnik = max(dzielniki.values())
        wynik = 0
            
        for i in dzielniki:
            if dzielniki[i] == najwiekszyDzielnik:
                wynik = max(wynik,i)
        print(wynik)
        
main()