from itertools import accumulate as ac

def fast(n, l):
    sumy = list(ac(l))
    max_w = 1e18

    for i in range(n - 1):
        po_lewo = sumy[i]
        po_prawo = sumy[-1] - sumy[i]
        
        if abs(po_prawo - po_lewo) < max_w:
            max_w = abs(po_prawo - po_lewo)
            
    return max_w

def sumuj(od, do, l):
    suma = 0
    
    for i in range(od, do):
        suma += l[i]
    
    return suma

def brut(n, l):
    max_w = 1e18

    for i in range(n - 1):
        po_lewo = sumuj(0, i + 1, l)
        po_prawo = sumuj(i + 1, n, l)
        
        if abs(po_prawo - po_lewo) < max_w:
            max_w = abs(po_prawo - po_lewo)
           
    return max_w
            
import random
licz = 1

while True:
    n = random.randint(1, int(1e4))
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(-1000, 1000)
        
    w1, w2 = brut(n, a), fast(n, a)
    
    if w1 == w2:
        print(licz, "test : OK")
    else:
        print(licz, "test : ŹLE")
        print("BRUT:", w1)
        print("FAST:", w2)
        print("")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        break
        
    licz += 1