# https://szkopul.edu.pl/c/oki-wakacje-2023/p/owc/

from heapq import heapify, heappop
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

@dataclass
class Miasto:
    nazwa : str
    cena : int
    widok : int
    odl_od_dom : int
    stars : int
    lit : str
    
    def __lt__(self, other):
        if self.lit == "C":
            return self.cena < other.cena
        elif self.lit == "W":
            return self.widok > other.widok
        elif self.lit == "O":
            return self.odl_od_dom < other.odl_od_dom
        else:
            return self.stars > other.stars
    

def main():
    lit, n = map(str, input().split())
    n = int(n)
    kol = []
    
    for _ in range(n):
        a, b, c, d, e = map(str, input().split())
        kol.append(Miasto(a, int(b), int(c), int(d), int(e), lit))
        
    heapify(kol)
    miasto = heappop(kol)
    w = []
    w.append(miasto.nazwa)
    naj = 0
    
    if lit == "C":
        naj = miasto.cena
    elif lit == "W":
        naj = miasto.widok
    elif lit == "O":
        naj = miasto.odl_od_dom
    else:
        naj = miasto.stars
    
    takie_same = True
    
    while takie_same and len(kol) > 0:
        miasto = heappop(kol)
        
        if lit == "C":
            if miasto.cena > naj:
                takie_same = False
            else:
                w.append(miasto.nazwa)
        elif lit == "W":
            if miasto.widok < naj:
                takie_same = False
            else:
                w.append(miasto.nazwa)
        elif lit == "O":
            if miasto.odl_od_dom > naj:
                takie_same = False
            else:
                w.append(miasto.nazwa)
        else:
            if miasto.stars < naj:
                takie_same = False
            else:
                w.append(miasto.nazwa)
                
    if lit == "C":
        print("Najnizsza cena: ", end = "")
    elif lit == "W":
        print("Najlepszy widok: ", end = "")
    elif lit == "O":
        print("Najmniejsza odleglosc: ", end = "")
    else:
        print("Najwiecej gwiazdek: ", end = "")
        
    print(naj)
    
    print("Miasta: ", end = "")
    
    for i in w:
        print(i, end = " ")
        
        
    
    
main()