# https://szkopul.edu.pl/c/testowy_dd/p/prz2/18871/

from math import sqrt
from sys import stdin
input = stdin.readline     

def pierw(N):
    dzielnik = 2
    w = []
    
    while dzielnik * dzielnik <= N:
        if N % dzielnik == 0:
            N //= dzielnik
            w.append(dzielnik)
        else:
            dzielnik += 1
            
    if N > 1:
        w.append(N)
    
    return w

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l, reverse = True)
    MAXN = 13
    czy_moze = [True for _ in range(MAXN)]
    czy_moze[0] = False
    czy_moze[1] = False
    czy_bylo = set()
    
    for i in range(n):
        liczba = l[i]
        
        pier = list(set(pierw(liczba)))
        
        for d in pier:
            if d not in czy_bylo:
                czy_bylo.add(d)
                od = d
        
                for k in range(od, MAXN, od):
                    czy_moze[k] = False
            
                
    for i in range(MAXN):
        if czy_moze[i]:
            print(i)
            return 
    
main()