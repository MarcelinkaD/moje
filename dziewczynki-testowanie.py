def fast(n, k, l):
    min_w = 1e18
    glowa = -1
    ogon = 0
    ld, lc = 0, 0
    
    while ogon < n - 1:
        while glowa < n - 1 and ld != k:
            glowa += 1
            
            if l[glowa] == 0:
                ld += 1
            else:
                lc += 1
                
            if ld == k:
                min_w = min(lc, min_w)
            
        if l[ogon] == 0:
            ld -= 1
        else:
            lc -= 1
                
        if ld == k:
            min_w = min(lc, min_w)
                
        ogon += 1
                
    if min_w != 1e18:
        return min_w
    else:
        return "NIE"
    
    
def brut(n, k, l):
    w = 1e18
    if l == [0]:
        return "NIE"
    
    for i in range(n):
        ld = 0
        lc = 0
        for j in range(i, n):
            if l[j] == 0:
                ld += 1
            else:
                lc += 1
                
            if ld == k:
                w = min(w, lc)
                break
            
    if w != 1e18:
        return w
    else:
        return "NIE"


import random as rd
licz = 1

while True:
    n = rd.randint(1, 10)
    k = rd.randint(1, n)
    l = []
    
    for _ in range(n):
        l.append(rd.randint(0, 1))
        
    wyn1, wyn2 = brut(n, k, l), fast(n, k, l)
    
    if wyn1 == wyn2:
        print(licz, "Test:", "OK")
    else:
        print(licz, "Test:", ":-(")
        print("Wynik bruta:", wyn1)
        print("Wynik fasta:", wyn2)
        print(n, k)
        
        for i in l:
            print(i, end = " ")
        break
                        
        
        
    licz += 1
    



    
    
    
    
