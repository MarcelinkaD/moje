# https://szkopul.edu.pl/c/olimpiada-od-podstaw-2023-24/p/bpw/

from sys import stdin
from dataclasses import dataclass
input = stdin.readline

@dataclass
class brygada:
    liczba : int
    suma : int

def main():
    n = int(input())
    l = list(map(str, input().split()))
    wyn = []
    
    for i in l:
        sumka = 0
        for k in i:
            sumka += int(k)
        
        ch = brygada(int(i), sumka)
        wyn.append(ch)
        
    wyn.sort(key = lambda x: (x.suma, x.liczba), reverse=True)
    
    for i in wyn:
        print(i.liczba, end = " ")
    
main()