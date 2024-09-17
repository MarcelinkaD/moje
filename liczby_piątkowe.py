# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/lip/

import bisect as bi
from sys import stdin
input = stdin.readline

def potega(x, y):
    if y == 0:
        return 1
    
    if y % 2 == 1:
        return x * potega(x, y - 1)
    
    p = potega(x, y // 2)
    
    return p * p

def main():
    piat = []
    do = potega(2, 20)
    max_potega = 20
    kol_pot = [1]
    
    while kol_pot[-1] <= 10**14:
        kol_pot.append(kol_pot[-1] * 5)
    
    for maska in range(1, 1 << 20):
        num = 0
        for i in range(20):
            if maska & (1 << i):
                num += kol_pot[i]
        piat.append(num)
    
    piat = sorted(piat)

    q = int(input())
    
    for _ in range(q):
        od, do = map(int, input().split())
        gdzie_od = bi.bisect_left(piat, od)
        gdzie_do = bi.bisect_right(piat, do)
        
        print(gdzie_do - gdzie_od) 
    
main()