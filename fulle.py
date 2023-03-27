# OIJ XVII

from collections import Counter as C
from itertools import product
from sys import stdin
input = stdin.readline

def main():
    rodzaje = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    lr = len(rodzaje)
    karty = str(input().strip())
    c = C(karty)
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
                
    lista1 = [i for i in range(0, ile_3 + 1)]
    lista2 = [i for i in range(0, ile_4 + 1)]
    kom = product(lista1, lista2)
    w = -1
    
    for i in kom:
        x, y = i[0], i[1]
        w = max(w, min(ile_3 - x + ile_2 + 2 * (ile_4 - y), x + y))
        
    print(w)
    
main()

