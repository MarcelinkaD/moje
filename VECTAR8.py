def czy_bylo_zero(liczbaj):
    liczbaS = str(liczbaj)
    for k in liczbaS:
        if(k == "0"):
            return True
    return False

liczba_zapytan = int(input())
MAXN = int(1e6 + 1)
sito = [False] * MAXN
sito[1] = True

for i in range(2, MAXN):
    if sito[i] == False:
        for k in range(i * i, MAXN, i):
            sito[k] = True

for i in range(liczba_zapytan):
    liczba = int(input())
    wynik = 0
    for k in range(1, liczba + 1):
        if(sito[k] == False):
            if(czy_bylo_zero(liczba) == False):
                wynik += 1
    print(wynik)

