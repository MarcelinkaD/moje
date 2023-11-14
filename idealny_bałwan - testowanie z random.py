def czy_da_sie(r, limit):
    r2 = r ** 2
    v = 14 * r2
    return v <= limit

def brut(n):
    max_w = -1
    
    for i in range(n - 1, -1, -1):
        if czy_da_sie(i, n):
            max_w = i
            break
        
    h = 12 * max_w
    
    return h

def fast(limit):
    start, stop = 1, limit
    max_r = -1
    
    while start < stop:
        r = (start + stop) // 2
        if czy_da_sie(r, limit):
            max_r = max(r, max_r)
            start = r + 1
        else:
            stop = r
            
    h = 12 * max_r
    
    return h

def brut2(N):
    R = int((N / 14)**0.5)
    while R > 0:
        potrzebne_wiadra = R**2 + (2*R)**2 + (3*R)**2
        
        if potrzebne_wiadra <= N:
            return 2*R + 4*R + 6*R
        
        R -= 1
    

    return 0
    
    
    
import random

numer_testu = 1
while True:
    n = random.randint(14, 1000000)
    
    [wynik1, wynik2, wynik3] = [brut(n), fast(n), brut2(n)]
    if wynik1 == wynik2 and wynik2 == wynik3:
        print("Test " + str(numer_testu) + "     OK")
    else:
        print("Test " + str(numer_testu) + "     ZLA ODPOWIEDZ")
        print("\nwejscie:")
        print(n)
        print("\n\nwynik 1 bruta:         " + str(wynik1))
        print("\n\nwynik 2 bruta:         " + str(wynik3))
        print("\nwynik wzorcowki:     " + str(wynik2))
        
        
        break
    
    numer_testu += 1    