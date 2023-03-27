import bisect as bi

def fast(n, l):
    l.sort()
    maxi = l[n - 1]
    w = 0
    baj = 2
    czy_bylo = [False for _ in range(n)]
    
    while baj < maxi:
        gdzie = bi.bisect_left(l, baj)
        index = gdzie - 1
        if czy_bylo[index] == False and index != -1:
            baj += l[index]
            w += 1
            czy_bylo[index] = True
        else:
            while index != -1 and czy_bylo[index]:
                index -= 1
            
            if index == -1:
                break
            else:
                baj += l[index]
                w += 1
                czy_bylo[index] = True
    
    if baj >= maxi:
        return w
    else:
        return "NIE"
    
def brut(n, l):
    l.sort()
    w = 0
    baj = 2
    maxi = max(l)
    
    if l[0] > 2:
        return "NIE"
        return 
    
    while baj < maxi:
        for i in range(len(l) + 1):
            if l[i] >= baj:
                index = i - 1
                if index == -1:
                    return "NIE"
                    return
                baj += l[i - 1]
                w += 1
                l.remove(l[i - 1])
                break

    if baj >= maxi:
        return w
    else:
        return "NIE"


import random

numer_testu = 1
while True:
    n = random.randint(1, 10)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 20)
    
    
    tab1 = a.copy()
    tab2 = a.copy()
    
    [wynik2, wynik1] = [fast(n, tab1), brut(n, tab2)]
    if wynik1 == wynik2:
        print("Test:", numer_testu, "OK")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("wejscie:")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        print("\nwynik bruta:         " + str(wynik1))
        print("wynik wzorcowki:     " + str(wynik2))
        
        break
    
    numer_testu += 1