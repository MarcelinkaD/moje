def czypo(i, ost_wymaxowanie):
    if ost_wymaxowanie == -1:
        return False
    
    if ost_wymaxowanie < i:
        return True
    
    return False


def fast(n, q, l):
    w = [0 for _ in range(n)]
    maxi = -1
    ost_maxi = -1
    czy_byl_od_zmaxowania = set()
    ost_wymaxowanie = -1
    
    for i in range(q):
        if l[i] != n + 1:
            if czypo(i, ost_wymaxowanie) and l[i] not in czy_byl_od_zmaxowania:
                w[l[i] - 1] = ost_maxi + 1
                czy_byl_od_zmaxowania.add(l[i])
            else:
                w[l[i] - 1] += 1
            maxi = max(maxi, w[l[i] - 1])
        else:
            czy_byl_od_zmaxowania = set()
            ost_wymaxowanie = i
            ost_maxi = maxi
            
            
    for i in range(n):
        if i + 1 not in czy_byl_od_zmaxowania and ost_wymaxowanie != -1:
            w[i] = ost_maxi
        
    return w

def brut(n, q, l):
    maxi = -1
    w = [0 for _ in range(n)]
    
    for i in l:
        if i != n + 1:
            w[i - 1] += 1
            maxi = max(maxi, w[i - 1])
        else:
            w = [maxi for _ in range(n)]
            
    return w

import random

numer_testu = 1
while True:
    n = random.randint(1, 5)
    q = random.randint(1, 10)
    l = []
    for i in range(q):
        l.append(random.randint(1, n + 1))
    
    [wynik1, wynik2] = [brut(n, q, l), fast(n, q, l)]
    if wynik1 == wynik2:
        print("Test: " + str(numer_testu) + " OK")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("\nwejscie:")
        print(n, q)
        for i in range(q):
            print(l[i], end = ' ')
        print("\n\nwynik bruta:         " + str(wynik1))
        print("\nwynik wzorcowki:     " + str(wynik2))
        
        break
    
    numer_testu += 1