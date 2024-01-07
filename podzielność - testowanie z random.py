from itertools import permutations

def gen(lit, k, akt):
    if not lit:
        if int(akt) % k == 0:
            return 1
        return 0
    
    wyn = 0
    czy = set()
    for i in range(len(lit)):
        litera = lit[i]
        if litera not in czy:
            wyn += gen(lit[:i] + lit[i+1:], k, akt + lit[i])
            czy.add(litera)
        
    return wyn

def fast(n, k):
    k = int(k)
    lit = []
    
    for i in n:
        lit.append(i)
    
    w = gen(lit, k, "")
    
    return w

def brut(n, k):
    k = int(k)
    permList = permutations(str(n))        
    w = 0
    uni = set()
    
    for i in permList:
        nowa = int("".join(i))
        if nowa % k == 0 and nowa not in uni:
            w += 1
            uni.add(nowa)
            
    return w
    
    
import random

numer_testu = 1
while True:
    n = random.randint(1, 10000)
    k = random.randint(2, 10)
    
    [wynik1, wynik2] = [brut(str(n), k), fast(str(n), k)]
    if wynik1 == wynik2:
        print(numer_testu, "- OK")        
    else:
        print(numer_testu, "- ŹLE")
        print("\n")
        print(n, k)
        print(wynik1, " - brut")
        print(wynik2, " - wzorcówka")
        
        break
    
    numer_testu += 1 