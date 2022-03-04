from sys import stdin
input = stdin.readline
from dataclasses import dataclass

@dataclass
class punkt:    
    x: int
    y: int
    pkt: int
    
def main():
    liczba_punktow = int(input())
    wyprawa = []
    kalorie = 0
    nastepny_pkt = 0
    
    for i in range(liczba_punktow):
        x, y = map(int, input().split())
        wyprawa.append(punkt(x, y, i + 1))
        
    for pt in range(len(wyprawa) - 1):
        nastepny_pkt = pt + 1
        
        
        if wyprawa[pt].x > wyprawa[nastepny_pkt].x:
            kalorie += wyprawa[pt].x - wyprawa[nastepny_pkt].x
        else:
            kalorie += wyprawa[nastepny_pkt].x - wyprawa[pt].x
            
        if wyprawa[pt].y < wyprawa[nastepny_pkt].y:
            kalorie += wyprawa[nastepny_pkt].y - wyprawa[pt].y
            
    print(kalorie)
    
main()