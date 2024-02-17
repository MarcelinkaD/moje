# https://szkopul.edu.pl/c/testowy_dd/p/ful/

from collections import Counter as C
from itertools import product
from sys import stdin
input = stdin.readline

def main():
    rodzaje = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    lr = len(rodzaje)
    karty = str(input().strip())
    c = dict(C(karty))
    naj_w = 0
    ile_2 = 0
    ile_3 = 0
    ile_4 = 0
    
    for i in range(lr):
        if rodzaje[i] in c:
            if c[rodzaje[i]] % 4 == 0:
                ile_4 += c[rodzaje[i]] // 4
            elif c[rodzaje[i]] % 2 == 0:
                ile_2 += c[rodzaje[i]] // 2
            elif c[rodzaje[i]] % 3 == 0:
                ile_3 += c[rodzaje[i]] // 3
    
    for ile_3_z_3 in range(ile_3 + 1):
        for ile_3_z_4 in range(ile_4 + 1):
            liczba_fulli = min(ile_2 + ile_3 - ile_3_z_3 + 2 * ile_4 - 2 * ile_3_z_4, ile_3_z_3 + ile_3_z_4)
            naj_w = max(liczba_fulli, naj_w)
            
    print(naj_w)
    
    
main()

