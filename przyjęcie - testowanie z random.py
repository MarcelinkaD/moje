def fast(l):
    l = list(set(l))
    i = 1
    
    while True:
        zle = False
        for k in l:
            if k % i == 0:
                zle = True
                break
        
        if zle == False:
            return i
        
        i += 1

def brut(l):
    i = 1
    
    while True:
        zle = False
        for k in l:
            if k % i == 0:
                zle = True
                break
        
        if zle == False:
            return i
        
        i += 1
        
import random
licz = 1

while True:
    n = random.randint(1, 10)
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = random.randint(1, 5)
        
    w1, w2 = brut(a), fast(a)
    
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