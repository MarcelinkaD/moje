# https://szkopul.edu.pl/c/programowanie-od-podstaw-2022-23/p/gra/

from heapq import heapify, heappop, heappush
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class Literka:
    litera : str
    
    def __lt__(self, other):
        return self.litera < other.litera

def main():
    n = int(input())
    kol = []
    stef = list(map(str, input().split()))
    k = int(input())
    wal = list(map(str, input().split()))
    
    for i in stef:
        kol.append(Literka(i))
        
    heapify(kol)
    
    for i in wal:
        heappush(kol, Literka(i))
        lit = heappop(kol)
        print(lit.litera, end = " ")
    
main()