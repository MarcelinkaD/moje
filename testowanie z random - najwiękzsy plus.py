def czy_da_sie(ra, li):
    for i in range(ra, len(li) - ra):
        if li[i] >= (ra + ra + 1):
            czy_zle = False
            for k in range(1, ra + 1):
                if li[i - k] < (ra + 1) or li[i + k] < (ra + 1):
                    czy_zle = True
                    break
                
            if czy_zle:
                continue
            
            return True
        
    return False

def binary(maxi, li):
    pocz = 0
    kon = maxi
    
    while pocz < kon:
        srodek = (pocz + 1 + kon) // 2
        if czy_da_sie(srodek, li):
            pocz = srodek
        else:
            kon = srodek - 1
        
    return pocz

def fast(n, wierz):
    maxi = max(wierz)
    
    return binary(maxi, wierz)

def brut(n, wie):
    w = 0
    
    while czy_da_sie(w, wie):
        w += 1
    
    return w - 1


import random

numer_testu = 1
while True:
    n = random.randint(1, 10)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 20)
    
    [wynik1, wynik2] = [brut(n, a), fast(n, a)]
    if wynik1 == wynik2:
        print("Test: " + str(numer_testu) + " Jest git")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("\nwejscie:")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        print("\n\nwynik bruta:         " + str(wynik1))
        print("\nwynik wzorcowki:     " + str(wynik2))
        
        break
    
    numer_testu += 1