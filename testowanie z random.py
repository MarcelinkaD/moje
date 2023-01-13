def brut(n, l):
    w = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1 , n):
                if l[i] + l[j] > l[k] and  l[k] + l[j] > l[i] and l[i] + l[k] > l[j]:
                    w += 1
                    
    return w

def fast(n, l):
    l = sorted(l)
    w = 0
    c = n - 1
    
    while c >= 2:
        a = 0
        b = c - 1
        while a < b:
            if l[a] + l[b] > l[c]:
                w += b - a
                b -= 1
            else:
                a += 1
            
        c -= 1
          
    return w



import random

numer_testu = 1
while True:
    n = random.randint(1, 10)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 10**9)
    
    [wynik1, wynik2] = [brut(n, a), fast(n, a)]
    if wynik1 == wynik2:
        print("Test " + str(numer_testu) + "     OK")
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