def brut(n, l):
    min_w = 1e18
    
    for i in range(n):
        for k in range(i + 1, n):
            zlicz = {}
            czy_jest = False
            
            for j in range(i, k + 1):
                if l[j] not in zlicz:
                    zlicz[l[j]] = 0
                zlicz[l[j]] += 1
                
                if zlicz[l[j]] >= 3:
                    czy_jest = True
                    
            if czy_jest:
                min_w = min(min_w, k - i + 1)
    
    if min_w == 1e18:
        return "NIE"
    else:
        return min_w
    
def fast(n, l):
    min_w = 1e18
    wystapienia = {}
    
    for i in range(n):
        if l[i] not in wystapienia:
            wystapienia[l[i]] = []
        wystapienia[l[i]].append(i)
        
        if len(wystapienia[l[i]]) >= 3:
            akt_len = len(wystapienia[l[i]])
            odleglosc = i - wystapienia[l[i]][akt_len - 3] + 1
            min_w = min(min_w, odleglosc)
            
    if min_w == 1e18:
        return "NIE"
    else:
        return min_w
    
import random
licz = 1

while True:
    n = random.randint(1, 50)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, int(1e2))
        
    w1, w2 = brut(n, a), fast(n, a)
    
    if w1 == w2:
        print(licz, "test : OK")
    else:
        print(licz, "test : ŹLE")
        print("BRUT:", w1)
        print("FAST:", w2)
        print("")
        print(n)
        for i in range(n):
            print(a[i], end = ' ')
        break
        
    licz += 1