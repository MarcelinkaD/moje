from sys import stdin
input = stdin.readline

def BS(lo, hi, val, positions):
    while (lo < hi):
        mid = (lo + hi) // 2 
        if (positions[mid] <= val):
            hi = mid
        else:
            lo = mid + 1

    return lo

def main():
    dlugosc_korytarza, liczba_przyjaciol = map(int, input().split())
    korytarz = list(map(int, input().split()))
    min_kor = min(korytarz)
    nowy_korytarz = []
    nowy_korytarz.append(korytarz[0])
    poprzedni_dodany = korytarz[0]

    for k in range(1, dlugosc_korytarza):
        poprzedni = korytarz[k - 1]
        if(poprzedni > korytarz[k] and poprzedni_dodany > korytarz[k]):
            nowy_korytarz.append(korytarz[k])
            poprzedni_dodany = korytarz[k]

    for i in range(liczba_przyjaciol):
        przyjaciel = int(input())
        wynik = 0
        if(min_kor >= przyjaciel):
            print(wynik)
            continue

        pozycja = BS(0, len(nowy_korytarz), przyjaciel, nowy_korytarz)
        if(przyjaciel == nowy_korytarz[pozycja]):
            print(len(nowy_korytarz) - pozycja - 1)
        else:
            print(len(nowy_korytarz) - pozycja)
    
    
main()