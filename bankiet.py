# https://szkopul.edu.pl/problemset/problem/NQamRQ2UZEwn6gPqo-l6nat9/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    kto = {}
    
    for i in range(n):
        os = int(input())
        kto[i + 1] = os
    
    w = 0
    odw = set()
    
    for i in range(1, n + 1):
        if i not in odw:
            start = i
            akt = i
            odw.add(start)
            while kto[akt] != start:
                odw.add(kto[akt])
                akt = kto[akt]
            w += 1
                
    print(w)
    
main()