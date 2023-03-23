# https://szkopul.edu.pl/c/testowy_dd/p/wie/18801/

import bisect as bi
from sys import stdin
input = stdin.readline

def fast(n, m, schodki, ludki):
    maxi = -1
    
    for i in range(n):
        maxi = max(schodki[i], maxi)
        schodki[i] = maxi
        
    w = []
    
    for i in ludki:
        gdzie = bi.bisect_left(schodki, i)
        w.append(gdzie)
                     
    return w
        
def brut(n, m, schodki, ludki):
    w = []
    for i in range(m):
        czy_break = False
        for k in range(n):
            if ludki[i] <= schodki[k]:
                czy_break = True
                break
            
        if czy_break:
            w.append(k)
        else:
            w.append(k + 1)
            
    return w

l = 1
import random as rd

while True:
    n = rd.randint(1, 10)
    m = rd.randint(1, n)
    schodki = []
    ludki = []
    
    for _ in range(n):
        schodki.append(rd.randint(1, 10))
        
    for _ in range(m):
        ludki.append(rd.randint(1, 10))
        
    wyn1, wyn2 = brut(n, m, schodki, ludki), fast(n, m, schodki, ludki)
    
    if wyn1 == wyn2:
        print(l, "Test:", "OK")
    else:
        print(l, "Test:", ":-(")
        print("Wynik bruta:", wyn1)
        print("Wynik fasta:", wyn2)
        print(n, m)
        
        for i in schodki:
            print(i, end = " ")
        print("")
        for i in ludki:
            print(i, end = " ")
            
        break
        
    l += 1
    


