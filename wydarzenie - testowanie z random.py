def brut(n, osoby, m, od_kogo):
    w = 0
    czy_byl = set()
    
    for i in range(m):
        if osoby[od_kogo[i] - 1] == 0:
            if od_kogo[i] not in czy_byl:
                w += 1
                czy_byl.add(od_kogo[i])
        else:
            akt = od_kogo[i]
            
            while osoby[akt - 1] != 0:
                akt = osoby[osoby[akt - 1] - 1]
            
            if od_kogo[akt - 1] not in czy_byl:
                w += 1
                czy_byl.add(od_kogo[akt - 1])
                
    return w

def fast(n, osoby, m, od_kogo):
    graf = [[] for _ in range(n + 1)]
    byli = set()
    w = 0
    
    for i in range(n):
        if osoby[i] != 0:
            graf[i + 1].append(osoby[i])
    
    for i in range(m):
        if osoby[od_kogo[i] - 1] == 0:
            if od_kogo[i] not in byli:
                w += 1
                byli.add(od_kogo[i])
        else:
            zrodlo = BFS(od_kogo[i] - 1, graf, n)
            
            if zrodlo not in byli:
                w += 1
                byli.add(zrodlo)
    
    return w

import random
licz = 1

while True:
    n = random.randint(1, 5)
    m = random.randint(1, n)
    a = [0 for i in range(n)]
    k = [0 for i in range(m)]
    for i in range(n):
        a[i] = random.randint(0, n)
    
    czy_bylo = set()
    for i in range(m):
        while k[i] not in czy_bylo
        k[i] = random.randint(1, n)
        
        czy_bylo.add(k[i])
        
        
    w1, w2 = brut(n, a, m, k), fast(n, a, m, k)
    
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
