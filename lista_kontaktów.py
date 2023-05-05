# https://codeshare.io/Ad9Yvk - algorytmika 19.04

from sys import stdin
input = stdin.readline

import queue as q

def BFS(kon, od, do):
    nieod = q.Queue()
    nieod.put(od)
    
    while not nieod.empty():
        osoba = nieod.get()
        for kolega in kon[osoba]:
            if kolega != do:
                nieod.put(kolega)
            else:
                return "TAK"
            
    return "NIE"

def main():
    n, k = map(int, input().split())
    kon = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        kon[a].append(b) 
        
    q = int(input())
    
    for _ in range(q):
        od, do = map(int, input().split())
        wyn = BFS(kon, od, do)
        print(wyn)
    
main()