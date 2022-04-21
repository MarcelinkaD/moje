from sys import stdin
from collections import Counter
input = stdin.readline

def sil(n):
    wynik = 1
    czy_za_duzy = False
    for i in range(2, n+1):
        wynik *= i
        if wynik >= 10000:
            czy_za_duzy = True
            wynik = wynik % 10000
            
    return wynik, czy_za_duzy

def main():
    liczba_zolnierzy = int(input())
    zolnierze = list(map(int, input().split()))
    ile_wzrostu = Counter(zolnierze)
    w = 1
    razy_co = 0
    nik = ""
    licz_wz = 0
    czy_za_duza = False
    
    for wzrost in ile_wzrostu:
        liczba_zol = ile_wzrostu[wzrost]
        licz_wz += 1
        
        if liczba_zol > 1:
            razy_co, czy_za_duza_sil = sil(liczba_zol)
            
            if czy_za_duza_sil:
                czy_za_duza = True
            
            w *= razy_co
            if w >= 10000:
                czy_za_duza = True
                w = w % 10000
        
            
    if licz_wz != 1:
        wy = (w * 2) % 10000
    else:
        wy = w % 10000
    
    if czy_za_duza == True:
        if wy < 10:
            print("000" + str(wy))
        elif wy < 100:
            print("00" + str(wy))
        elif wy < 1000:
            print("0" + str(wy))
        else:
            print(wy)
    else:
        print(wy)
        
main()