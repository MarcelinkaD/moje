import math

def dziel(x):
    wyn = set([x])
    
    for d in range(2, int(math.sqrt(x)) + 1):
        if x % d == 0:
            wyn.add(d)
            wyn.add(x // d)
            
    return wyn

def dzieln(x):
    wyn = set()
    
    for d in range(2, x + 1):
        if x % d == 0:
            wyn.add(d)
            
    return wyn

def fast(n, k):
    wykreslone = set([1])
    
    for i in range(n, n - k, -1):
        dzielniki = list(dziel(i))
        
        for i in dzielniki:
            wykreslone.add(i)
            
    w = 2
    
    while w <= n:
        if w not in wykreslone:
            return w
        
        w += 1
    
    return -1
    
def brut(n, k):
    wykreslone = set([1])
    
    for i in range(n, n - k, -1):
        dzielniki = list(dzieln(i))
        
        for i in dzielniki:
            wykreslone.add(i)
            
    w = 2
    
    while w <= n:
        if w not in wykreslone:
            return w
        
        w += 1
    
    return -1

import random
licz = 1

while True:
    n = random.randint(1, 10)
    a = random.randint(1, n)
        
    w1, w2 = brut(n, a), fast(n, a)
    
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