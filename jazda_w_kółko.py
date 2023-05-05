# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/bra/18442/

from sys import setrecursionlimit
from sys import stdin
input = stdin.readline
setrecursionlimit(1000000)

def DFS(wie, graf, odw, pop):
    odw.add(wie)
    for sasiad in graf[wie]:
        if sasiad not in odw:
            DFS(sasiad, graf, odw, wie)
        else:
            if pop != sasiad:
                return "TAK"
        
def main():
    n, m = map(int, input().split())
    graf = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graf[a].append(b)
        graf[b].append(a)
    
    for i in range(1, n + 1):
        if len(graf[i]) != 0:
            odw = set()
            w = DFS(i, graf, odw, i)
            
            if w != None:
                print(w)
                return
            
    print("NIE")
        
    
main()