import math
from itertools import accumulate
from dataclasses import dataclass
from sys import stdin
input = stdin.readline

def potega(a, x, n):
    if x == 0:
        return 1
    
    wynik = potega(a, x // 2, n)
    wynik = (wynik * wynik) % n
    
    if x % 2 == 1:
        wynik = (wynik * a) % n
        
    return wynik


def main():
	n = int(input())
	
	
main()
