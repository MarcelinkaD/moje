# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r5c/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    ile = {1: {"j" : 1, "e" : 2, "d" : 1, "n" : 1}, 2: {"d" : 1, "w" : 1, "a" : 1}, 3: {"t" : 1, "r" : 1, "z" : 1, "y" : 1}, 4: {"c" : 1, "z" : 1, "t" : 1, "e" : 1, "r" : 1, "y" : 1}, 5: {"p" : 1, "i" : 1, "e" : 1, "c" : 1}, 6: {"s" : 2, "z" : 1, "e" : 1, "c" : 1}, 7: {"s" : 1, "i" : 1, "e" : 2, "d" : 1, "m" : 1}, 8: {"o" : 1, "s" : 1, "i" : 1, "e" : 1, "m" : 1}, 9: {"d" : 1, "z" : 1, "i" : 2, "e" : 2, "w" : 1, "c" : 1}, 0: {"z" : 1, "e" : 1, "r" : 1, "o" : 1}}
    n = int(input())
    s = str(input().strip())
    c = dict(C(s))
    akt = 9
    licz = []
    
    while akt > -1:
        co_potrz = ile[akt]
        czy_da_sie = True

        for i in co_potrz:
            if i not in c or c[i] < co_potrz[i]:
                czy_da_sie = False
                akt -= 1
                break

        if czy_da_sie:
            for i in co_potrz:
                c[i] -= co_potrz[i]

            licz.append(akt)

          
    licz = sorted(licz, reverse = True)    
    for i in licz:
        print(i, end = "")
    
main()