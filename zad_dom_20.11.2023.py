from math import sqrt

def czy_pie(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return "NIE"
    return "TAK"

n = int(input())
pierwiastek = sqrt(n)

if int(pierwiastek) != pierwiastek:
    print("NIE")
else:
    now = int(pierwiastek)
    print(czy_pie(now))
    

import math

def ile_x(n, x):
    w = 0
    d = 2
    
    while d * d <= n:
        if n % d == 0:
            n //= d
            if d == x:
                w += 1
        else:
            d += 1
    
    if n > 1 and n == x:
        w += 1
    
    return w

n = int(input())
l = list(map(int, input().split()))
zlicz = {2 : 0, 5 : 0}

for i in range(n):
    zlicz[2] += ile_x(l[i], 2)
    zlicz[5] += ile_x(l[i], 5)
        
wyn = min(zlicz[5], zlicz[2])

print(wyn)
