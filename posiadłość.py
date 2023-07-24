# https://szkopul.edu.pl/c/testowy_dd/p/pos/

import math
from sys import stdin
input = stdin.readline

def cyfry_liczby(x):
    cyfry = []
    for _ in range(19):
        cyfry.append(x % 10)
        x //= 10
        cyfry = cyfry[::-1]
    return cyfry

def popraw(cyfry_a, cyfry_b):
    cyfry_c = list(cyfry_b)
    juz_dziewiatki = False
    for i in range(19):
        if juz_dziewiatki:
            cyfry_c[i] = 9
        elif cyfry_a[i] != cyfry_b[i]:
            cyfry_c[i] = cyfry_b[i] - 1
            juz_dziewiatki = True
    return cyfry_c

def main():
    a, b = map(int, input().split())
    cyfry_a, cyfry_b = cyfry_liczby(a), cyfry_liczby(b)
    cyfry_c = popraw(cyfry_a, cyfry_b)
    wynik1 = sum(cyfry_b)
    wynik2 = sum(cyfry_c)
    print(max(wynik1, wynik2))
            
main()