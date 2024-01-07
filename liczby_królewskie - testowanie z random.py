def czy_krol(x):
    jed = 0
    
    while x != 0:
        if x % 2 == 1:
            jed += 1
        x //= 2
        
    if jed % 2 == 0:
        return True
    return False

def fast(q, l):
    for i in range(q):
        n = l[i]
        
        l1 = 2 * n - 1
        l2 = 2 * n - 2
        
        if czy_krol(l1):
            return l1
        else:
            return l2
    

def brut(q, l):
    for i in range(q):
        n = l[i]
        akt_badana = 0

        while n != 0:
            jedynki = 0
            nowa = akt_badana
            
            while nowa != 0:
                if nowa % 2 == 1:
                    jedynki += 1
                nowa //= 2
            
            if jedynki % 2 == 0:
                n -= 1
                
                if n == 0:
                    return akt_badana
                
            akt_badana += 1
            
from random import randint
licz = 0

while True:
    licz += 1
    q = randint(1, 100)
    l = [randint(1, 1000) for _  in range(q)]
        
    w1, w2 = fast(q, l), brut(q, l)

    if w1 == w2:
        print("OK", licz)
    else:
        print("ZLE", licz)
        print("Fast:", w1)
        print("Brut:", w2)
        print("")
        print(q)
        
        for i in l:
            print(i, end = " ")
        print("")
        