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
    do = n
    
    for i in range(m):
        gdzie = bi.bisect_left(schodki, ludki[i], lo = 0, hi = do)
        do = max(gdzie - 1, 0)
        w.append(gdzie)
                     
    return w
        
def brut(n, m, schodki, ludki):
    w = []
    ostatni = n
    
    for i in range(m):
        wyn = 0
        for k in range(ostatni):
            if ludki[i] > schodki[k]:
                wyn = k + 1              
            else:                
                break

        ostatni = wyn - 1
        w.append(wyn)
            
            
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
    




