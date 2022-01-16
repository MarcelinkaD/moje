def main():
    mewy = str(input())
    mewyN = len(mewy)
    ilosc_zapytan = int(input())
    zapytania = list(map(int, input().split()))
    licznik = 1
    nowe_mewy = [0] * mewyN
    nowe_mewy[0] = 1
    nowe_mewyN = len(nowe_mewy)
    
    for i in range(1, mewyN):
        if(mewy[i] == mewy[i - 1]):
            licznik += 1
            nowe_mewy[i] = licznik
        else:
            licznik = 1
            nowe_mewy[i] = licznik
            
    nowy_licznik = nowe_mewy[nowe_mewyN - 1]
    poprzedniaMewa = nowe_mewy[nowe_mewyN - 1]
    
    for i in range(nowe_mewyN - 1, -1, -1):
 #       if(i < mewyN - 1 and mewy[i] != mewy[i + 1]):
  #          nowy_licznik = nowe_mewy[i]
            
        if(nowy_licznik > nowe_mewy[i] and poprzedniaMewa != 1):            
            nowe_mewy[i] = nowy_licznik
            
        poprzedniaMewa = nowe_mewy[i]
        
            
        
    for i in zapytania:
        print(nowe_mewy[i - 1], end = " ")
    
main()