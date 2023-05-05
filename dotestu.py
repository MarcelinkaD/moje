import math
import heapq
from collections import deque
from collections import Counter as C
from itertools import accumulate
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

def liczba_samoglosek(a, b, samogloski):
    c1, c2 = {}, {}
    for i in a:
        if i in samogloski:
            c1[i] = c1.get(i, 0) + 1
    for i in b:
        if i in samogloski:
            c2[i] = c2.get(i, 0) + 1
            
    return c1 == c2

def usun_spacje(x):
    return ''.join([i for i in x if i != ' '])

def main():
    n, k = map(int, input().split())
    w = 0
    samogloski = set(["a", "e", "i", "o", "u", "y"])
    
    for _ in range(n):
        a = str(input().strip())
        b = str(input().strip())
        a, b = usun_spacje(a), usun_spacje(b)
        
        if len(a) >= k and len(b) >= k:
            a = a[-k:]
            b = b[-k:]
            if liczba_samoglosek(a, b, samogloski):
                w += 1
                
    print(w)
    
main()

