# https://szkopul.edu.pl/problemset/problem/T3NYgJlRkL1PLU0m7N79-Wl2/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    c = {}
    w = []
    
    for _ in range(n):
        co, ile = map(str, input().split())
        ile = int(ile)
        
        if co not in c:
            c[co] = 0
            w.append(co)
        
        c[co] += ile
        
    w.sort()
    
    for i in w:
        print(i, end = " ")
        print(c[i])
    
main()