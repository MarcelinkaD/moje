def stworz_licz(x, dlugosc):
    akt_pot = 1
    wyn = 0
    
    while dlugosc > 0:
        wyn += akt_pot * x
        dlugosc -= 1
        akt_pot *= 10
        
    return wyn

def fast(n):
    w = []
    dlugosc = len(str(n))
    
    for i in range(1, 10):
        nowa_licz = stworz_licz(i, dlugosc)
        if n < nowa_licz:
            w.append(nowa_licz)
            break
        
    if len(w) == 1:
        for _ in range(3 - len(w)):
            i += 1
            if i < 10:
                nowa_licz = stworz_licz(i, dlugosc)
                w.append(nowa_licz)
    
    if len(w) < 3:
        i = 0
        dlugosc += 1
        for _ in range(3 - len(w)):
            i += 1
            nowa_licz = stworz_licz(i, dlugosc)
            w.append(nowa_licz)
            
    return [w[0], w[1], w[2]]

def czy_dobra(x):
    x = str(x)
    sett = set()
    
    for i in x:
        sett.add(i)
        
    if len(sett) == 1:
        return True
    return False

def brut(n):
    w = []
    akt_licz = n + 1
    
    while len(w) < 3:
        if czy_dobra(akt_licz):
            w.append(akt_licz)
        akt_licz += 1
        
    return [w[0], w[1], w[2]]
        

import random
licz = 1

while True:
    n = random.randint(1, 1000000)
        
    w1, w2 = brut(n), fast(n)
    
    if w1 == w2:
        print(licz, "test : OK")
    else:
        print(licz, "test : ŹLE")
        print("BRUT:", w1)
        print("FAST:", w2)
        print("")
        print(n, a)
        break
        
    licz += 1