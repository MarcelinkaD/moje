# https://sio2.mimuw.edu.pl/c/zwo21/p/tar/

from sys import stdin
input = stdin.readline

def binary(q, p):
    pocz = 0
    kon = q
    
    while pocz < kon:
        x = (pocz + 1 + kon) // 2
        if x ** 3 + p * x <= q:
            pocz = x
        else:
            kon = x - 1
        
    return pocz

def main():
    q = int(input())
    
    for _ in range(q):
        p, q = map(int, input().split())
        w = binary(q, p)
        
        if w ** 3 + p * w == q:
            print(w)
        else:
            print("NIE")
    
main()