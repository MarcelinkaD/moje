def oblicz_wyn(n):
    wyn = 0
    
    for i in range(1, n + 1):
        wyn += n - (n - i)
    
    return wyn

def f(lista, n):
    wyn = 0
    od = 0
    akt_w = 1
    milion = int(1e6)
    dlugosc = 0
    
    for i in range(n):
        akt_w *= lista[i]
        if akt_w < milion:
            dlugosc += 1
        else:
            wyn += oblicz_wyn(dlugosc)
            akt_w = lista[i]
            if lista[i] < milion:
                dlugosc = 1
            else:
                dlugosc = 0
            
    wyn += oblicz_wyn(dlugosc)   
    return wyn

def fast(n, l):
    w = 0
    l1 = []
    l2 = []
    
    for i in range(n):
        if i % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
            
    w += f(l1, len(l1))
    w += f(l2, len(l2))
                    
    return w

def brut(n, l):
    w = n
    
    for i in range(n):
        for k in range(i, n, 2):


import random
licz = 1

while True:
    n = random.randint(1, 3)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, n)
        
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