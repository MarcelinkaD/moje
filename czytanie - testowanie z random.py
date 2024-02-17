def brut(n, l):
    w = 0
    
    for i in range(n):
        ile = l[i]
        
        if ile > 10:
            while ile > 10:
                w += 1
                ile -= 10
            
    return w

def fast(n, l):
    w = 0
    
    for i in range(n):
        do_przeczytania = l[i]
        
        if do_przeczytania > 10:
            if do_przeczytania % 10 == 0:
                w += (do_przeczytania // 10) - 1
            else:
                w += do_przeczytania // 10        
        
    return w

import random
licz = 1

while True:
    n = random.randint(1, 1000)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 1000)
        
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