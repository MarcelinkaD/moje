# https://szkopul.edu.pl/problemset/problem/kwb/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    d = {}
    
    for _ in range(n):
        amogus = list(map(int, input().split()))
        
        for i in range(m):
            if amogus[i] != 0:
                if amogus[i] not in d:
                    d[amogus[i]] = 0
                d[amogus[i]] += 1
                
    w = 0
    max_w = -1
    
    for i in d:
        if d[i] > max_w:
            max_w = d[i]
            w = i
            
    print(w)        
    
main()