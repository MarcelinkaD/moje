# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r1c/

from sys import stdin
input = stdin.readline
        
def main():
    n, k = map(int, input().split())
    graf = [set() for _ in range(n + 1)]
    w = [0 for _ in range(n + 1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        
        if b not in graf[a]:
            graf[b].add(a)
            w[b] += 1
        else:
            w[a] -= 1
            
    for i in range(1, n + 1):
        print(w[i], end = " ")     

main()