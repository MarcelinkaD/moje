def inRange(x, n):
    if x < n and x > -1:
        return True
    return False

def brut(n, l):
    max_wyn = 0
    
    for i in range(n):
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
            
        akt_wyn = 0
        for k in range(1, n):
            if inRange(k - 1, n):
                if l[k - 1] == l[k]:
                    akt_wyn += 1
                    
        max_wyn = max(akt_wyn, max_wyn)
        
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
            
    return max_wyn

def fast(n, l):
    max_wyn = 0
    ile_par_od_i = [0 for _ in range(n)]
    
    for i in range(n):
        if inRange(i - 1, n):
            ile_par_od_i[i] = ile_par_od_i[i - 1]
            if l[i - 1] == l[i]:
                ile_par_od_i[i] += 1
                
    for i in range(n):
        if inRange(i + 1, n) and inRange(i - 1, n):
            if l[i] == l[i + 1]:
                if l[i - 1] == l[i]:
                    nowy_wyn = ile_par_od_i[-1] - 2
                else:
                    nowy_wyn = ile_par_od_i[-1]
            else:
                if l[i - 1] == l[i]:
                    nowy_wyn = ile_par_od_i[-1]
                else:
                    nowy_wyn = ile_par_od_i[-1] + 2
                
        elif inRange(i + 1, n):
            if l[i] == l[i + 1]:
                nowy_wyn = ile_par_od_i[-1] - 1
            else:
                nowy_wyn = ile_par_od_i[-1] + 1
        else:
            if l[i] == l[i - 1]:
                nowy_wyn = ile_par_od_i[-1] - 1
            else:
                nowy_wyn = ile_par_od_i[-1] + 1
            
        max_wyn = max(max_wyn, nowy_wyn)  
        
    return max_wyn

import random
licz = 1

while True:
    n = random.randint(1, 10)
    a = [random.randint(0, 1) for _ in range(n)]
        
    w1, w2 = brut(n, a), fast(n, a)
    
    if w1 == w2:
        print(licz, "test : OK")
    else:
        print(licz, "test : ŹLE")
        print("BRUT:", w1)
        print("FAST:", w2)
        print("")
        print(n)
        
        for i in a:
            print(i, end = " ")
        break
        
    licz += 1