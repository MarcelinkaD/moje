from sys import stdin
input = stdin.readline
from dataclasses import dataclass

@dataclass
class max_z_pkt:    
    wysokosc: int
    indeks: int


def main():
    liczba_pkt = int(input())
    pkt = []
    maks = 0
    maksk = 0
    w_prawo = [0] * liczba_pkt
    w_lewo = [0] * liczba_pkt
    
    for i in range(liczba_pkt):
        k = int(input())
        pkt.append(k)
        if pkt[i] > maksk:
            maksk = pkt[i]
            w_lewo[i] = maksk
        else:
            w_lewo[i] = maksk
        
    for i in range(liczba_pkt - 1, -1, -1):
        if pkt[i] > maks:
            maks = pkt[i]
            w_prawo[i] = maks
        else:
            w_prawo[i] = maks
            

        
            
    for i in range(liczba_pkt):
        print(w_lewo[i], end = " ")
        print(w_prawo[i])
        
   
    
main()
        