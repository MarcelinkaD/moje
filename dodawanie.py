# https://sio2.mimuw.edu.pl/c/zwo20/p/dod/

from sys import stdin
input = stdin.readline

def main():
    k, s = map(int, input().split())
    u = 0
    
    for i in range(1, k):
        u += i
    
    ns = s
    ns -= u
    podzielone = ns // k
    
    if (podzielone * k) + u == s:
        for i in range(podzielone, podzielone + k):
            print(i, end = " ")
    else:
        print("NIE")
    
main()