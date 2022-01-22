
def main():
    MAXN = int(1e6 + 7)
    sito = [0] * MAXN
    sito[1] = 1
    liczba_zapytan = int(input())
    
    for i in range(2, MAXN):
        if sito[i] == 0:
            sito[i] = i
            for k in range(i, MAXN, i):
                sito[k] = i
    
    for zapytanie in range(liczba_zapytan):
        badanaLiczba = int(input())
        wynik = 1

        czynniki = {}
        
        while(badanaLiczba != 1):
            d = sito[badanaLiczba]
            if d in czynniki:
                czynniki[d] += 1
            else:
                czynniki[d] = 1           
            
            badanaLiczba = int(badanaLiczba/d)
            
        
        for x in czynniki:
            if(czynniki[x] % 2 == 1):
                wynik *= x
            
            
        print(wynik)
 
        

main()