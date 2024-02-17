# https://sio2.mimuw.edu.pl/c/oij17-2/p/lab/

from heapq import heappop, heapify, heappush
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    kol = []
    heapify(kol)
    akt_bal = 0
    w = 0
    
    for i in range(n):
        if l[i] < 0:
            heappush(kol, l[i])

            
        akt_bal += l[i]

        if akt_bal < 0:
            co_zamienic = heappop(kol)
            akt_bal -= co_zamienic * 2
            w += 1
            
    print(w)
    
main()