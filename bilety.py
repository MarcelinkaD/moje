# https://codeshare.io/Ad9Yvk - algorytmika 19.04
from sys import stdin
input = stdin.readline

def main():
    from heapq import heapify, heappop, heappush
    n = int(input())
    kol = []
    w = 0
    
    heapify(kol)
    
    for _ in range(n):
        a, b = map(int, input().split())
        
        while b != 0:
            b -= 1
            heappush(kol, a)
            
        w += heappop(kol)
        
    print(w)
        
    
    
    
main()