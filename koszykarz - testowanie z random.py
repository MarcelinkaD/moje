def brut(akt, trzeba, m):
    i = 0
    
    while akt < trzeba:
        akt += m
        i += 1
        
    return i

def fast(akt, trzeba, m):
    pocz = 0
    kon = trzeba
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        ile = m * srodek
        
        if akt + ile > trzeba:
            kon = srodek
        elif akt + ile < trzeba:
            pocz = srodek + 1
        else:
            return srodek
    
    return pocz

import random
licz = 1

while True:
    akt = random.randint(1, 200)
    trzeba = random.randint(1, 1000000000)
    m = random.randint(1, 1000000000)
    
    w1, w2 = brut(akt, trzeba, m), fast(akt, trzeba, m)
    if w1 == w2:
        print(licz, "test : OK")
    else:
        print(licz, "test : ŹLE")
        print("BRUT:", w1)
        print("FAST:", w2)
        print("\n")
        print(akt, trzeba, m)
        break
    
    licz += 1