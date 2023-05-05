# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/par/

maxi = -1
from sys import setrecursionlimit
from sys import stdin
input = stdin.readline
setrecursionlimit(1000000)

def DFS(akt_wie, pop_wie, dp, graf):
    global maxi
    ost = 0
    for syn in graf[akt_wie]:
        if syn == pop_wie:
            continue
        
        DFS(syn, akt_wie, dp, graf)
        dp[akt_wie] = max(dp[akt_wie], dp[syn] + len(graf[akt_wie]) - 2)
        
        maxi = max(maxi, max(ost + dp[syn] + len(graf[akt_wie]) - 2, dp[syn] + len(graf[akt_wie]) - 1))
        
        ost = max(ost, dp[syn])
        
    dp[akt_wie] = max(dp[akt_wie], len(graf[akt_wie]) - 1)

def main():
    n = int(input())
    graf = [[] for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    global maxi
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graf[a].append(b)
        graf[b].append(a)
        
    DFS(1, 0, dp, graf)
    
    print(maxi)
    
main()
    