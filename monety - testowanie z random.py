def f(i, l, n):
    ile_sie_miesci = min(n, l[i])
    do_umieszczenia = ile_sie_miesci - i
    return do_umieszczenia

def fast(n, l):
    w = 1
    MOD = int(1e9) + 7
    l.sort()
    
    for i in range(n):
        w *= f(i, l, n) % MOD
        
    return w 

def gen(liczby, akt, l):
    if not liczby:
        for i in range(len(l)):
            if akt[i] > l[i]:
                return 0
        
        return 1
            
    w = 0 
    for i in range(len(liczby)):
        liczba = liczby[i]
        w += gen(liczby[:i] + liczby[i + 1 : len(liczby)], akt + [liczba], l)
        
    return w

def brut(n, l):
    w = gen([i + 1 for i in range(n)], [], l)
    return w


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