# https://szkopul.edu.pl/c/testowy_dd/p/regal/

from heapq import heapify, heappop, heappush
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class pudlo:
    napis : str
    dlugosc : int
    
    def __lt__(self, other):
        return self.dlugosc < other.dlugosc

def main():
    n = int(input())
    kol = []
    heapify(kol)
    
    for _ in range(n):
        s = str(input().strip())
        heappush(kol, pudlo(s, len(s)))
        
    while len(kol) != 0:
        co = heappop(kol)
        print(co.napis)

main()