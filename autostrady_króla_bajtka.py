# https://szkopul.edu.pl/problemset/problem/autostrady/site/?key=statement

from sys import stdin
input = stdin.readline
import queue as q

def bfs(od, do, graf):
    kolejka = q.Queue()
    odw = set()
    
    kolejka.put(od)
    
    while not kolejka.empty():
        u = kolejka.get()
        
        if u == do:
            return "TAK"
        
        if u in graf:
            for somsiad in graf[u]:
                if somsiad not in odw:
                    kolejka.put(somsiad)
                    odw.add(somsiad)
                
                
    return "NIE"

def main():
    n, m = map(int, input().split())
    graf = {}
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        if a not in graf:
            graf[a] = []
            
        graf[a].append(b)
        
        if b not in graf:
            graf[b] = []
            
        graf[b].append(a)
        
    q = int(input())
    
    for _ in range(q):
        od, do = map(int, input().split())
        print(bfs(od, do, graf))
        
    
main()


