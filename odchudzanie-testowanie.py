def fast(n, l):
    maxi = l[0]
    w = 0
    
    for i in range(1, n):
        w = max(w, maxi - l[i])
        maxi = max(maxi, l[i])
        
    return w

def brut(n, l):
    w = 0
    
    for i in range(n):
        for k in range(i + 1, n):
            w = max(w, l[i] - l[k])
            
    return w

import random as rd
licz = 1

while True:
    n = rd.randint(1, 10)
    l = []
    
    for _ in range(n):
        l.append(rd.randint(1, 100))
        
    wyn1, wyn2 = brut(n, l), fast(n, l)
    
    if wyn1 == wyn2:
        print(licz, "Test:", "OK")
    else:
        print(licz, "Test:", ":-(")
        print("Wynik bruta:", wyn1)
        print("Wynik fasta:", wyn2)
        print(n)
        
        for i in l:
            print(i, end = " ")
            
        break
                        
        
        
    licz += 1