def brut(n, l, od, do):
    wyn = 0
    ile_zero = 0
    
    for i in range(od - 1, do):
        if l[i] == 1:
            wyn += ile_zero
        else:
            ile_zero += 1
            
    return wyn

def fast(n, l, od, do):
    l.insert(0, 0)
    ile_zero = [0 for _  in range(n + 1)]
    
    for i in range(1, n + 1):
        ile_zero[i] = ile_zero[i - 1]
        if l[i] == 0:
            ile_zero[i] += 1
                
    wyn = 0
    
    for i in range(od, do + 1):
        if l[i] == 1:
            wyn += ile_zero[i] - ile_zero[od - 1]
            
    return wyn


import random
licz = 1

while True:
    n = random.randint(1, 5)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(0, 1)
        
    od = random.randint(1, n)
    do = random.randint(od, n)
    
        
    w1, w2 = brut(n, a, od, do), fast(n, a, od, do)
    
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