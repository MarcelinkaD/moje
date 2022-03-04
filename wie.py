from typing import Container
from sys import stdin
input = stdin.readline

def WyszukajBinarnie(tab, liczba, n):
    p = 0
    k = n 
    while p < k:
        srodek = int((k + p) / 2)
        if(liczba < tab[srodek]):
            k = srodek
        elif(liczba > tab[srodek]):
            p = srodek + 1
        else:
            return srodek
            break

    return k

def main():
    liczba_schodkow, liczba_mieszkancow = map(int, input().split())

    schodki = list(map(int, input().split()))

    mieszkancy = list(map(int, input().split()))
    dodanie = 0

    for schodek in range(1, liczba_schodkow):
        if(schodki[schodek] < schodki[schodek - 1]):
            dodanie = schodki[schodek - 1]
            schodki[schodek] = dodanie



    for ludzik in mieszkancy:
        if ludzik <= schodki[0]:
            print("0", end = " ")
            continue

        miejsce = WyszukajBinarnie(schodki, ludzik, liczba_schodkow)
        print(miejsce, end = " ")

main()