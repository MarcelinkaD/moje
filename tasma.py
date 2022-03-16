from sys import stdin
input = stdin.readline

def main():
    ile_zpytan = int(input())

    for k in range(ile_zpytan):
        n = int(input())
        tab = list(map(int, input().split()))

        maxOdlPocz = 0

        for i in range(n):
            if(tab[0] != tab[i]):
                maxOdlPocz = i

        maxOdlKoniec = 0

        for i in range(n - 1, -1, -1):
            if(tab[i] != tab[n - 1]):
                maxOdlKoniec = n - i - 1

        wynik = max(maxOdlKoniec, maxOdlPocz)

        if(wynik == 0):
            wynik = "BRAK"
            print(wynik)
        else:
            print(wynik)

main()