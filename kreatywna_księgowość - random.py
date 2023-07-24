from itertools import accumulate as ac

def suma(a, b, l):
    w = 0
    
    for i in range(a, b + 1):
        w += l[i]
    
    return w
    
def fast(n, m, l):
    pref = list(ac(l))
    w = -1e19
    
    for i in range(n):
        for k in range(i + 1, n):
            if i != 0:
                roznica = pref[k] - pref[i - 1]
            else:
                roznica = pref[k]
            po_mod = roznica % m
            w = max(w, po_mod)
    
    if w == -1e19:
        return 0
    else:
        return w

def brut(n, m, l):
    w = 0
    
    for i in range(n):
        for k in range(i + 1, n):
            s = suma(i, k, l)
            po_mod = s % m
            w = max(w, po_mod)
            
    return w
            
import random

numer_testu = 1
while True:
    n = random.randint(1, 10)
    m = random.randint(2, 15)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 20)
    
    [wynik1, wynik2] = [brut(n, m, a), fast(n, m, a)]
    if wynik1 == wynik2:
        print("Test " + str(numer_testu) + "  Jest git")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("\nwejscie:")
        print(n, m)
        for i in range(n):
            print(a[i], end = ' ')
        print("\n\nwynik bruta:         " + str(wynik1))
        print("\nwynik wzorcowki:     " + str(wynik2))
        
        break
    
    numer_testu += 1