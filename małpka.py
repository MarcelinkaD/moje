# https://sio2.mimuw.edu.pl/c/zwo20/p/mal/

import math
from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    
    print(n // math.gcd(n, k))
    
main()