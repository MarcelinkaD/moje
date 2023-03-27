# https://szkopul.edu.pl/c/testowy_dd/p/kol/

import heapq 
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class Osoba:
    wiek : int
    czas : int
    imie : str

    def __lt__(self, other):
        if self.wiek != other.wiek:
            return self.wiek < other.wiek;
        
        return self.czas < other.czas;
        

def main():
    n = int(input())
    kol = []
    
    for i in range(n):
        s = str(input().strip())
        if s != "-1":
            w, o = map(str, s.split())
            heapq.heappush(kol, Osoba(int(w), i, o))
        else:
            if kol:
                osoba = heapq.heappop(kol)
                print(osoba.imie)
            else:
                print("-")            
    
main()