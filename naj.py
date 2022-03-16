#Źródło https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

from sys import stdin
input = stdin.readline

def podziel_liste(lista, oddzialy):
    for i in range(0, len(lista), oddzialy): 
        yield lista[i : i + oddzialy]
        
def main():
    ciag_str = input().strip()
    liczby_do_rozdania = len(ciag_str)
    liczba_grop = int(input())
    ciag = []
    for i in range(len(ciag_str)):
        ciag.append(ciag_str[i])
        
    ciag.sort()
    
    wielkosc_grupy = len(ciag) // liczba_grop
    nowy_ciag = list(podziel_liste(ciag, liczba_grop))
    liczba = ""
    wynik = 0
    
    while "0" in nowy_ciag[0]:
        nowy_ciag[0].remove("0")
        nowy_ciag[1].insert(0, "0")
        
    while liczby_do_rozdania > 0:
        for i in range(len(nowy_ciag)):
            if len(nowy_ciag[i]) != 0:
                liczba += nowy_ciag[i][0]
                nowy_ciag[i].remove(nowy_ciag[i][0])
                liczby_do_rozdania -= 1
            else:
                continue
            
        wynik += int(liczba)
        
        liczba = ""
        
    print(wynik)
               
    
main()