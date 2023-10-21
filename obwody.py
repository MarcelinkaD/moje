# https://szkopul.edu.pl/problemset/problem/pCuYZIdhvWLrC2sVzkTiDdcl/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = []
    
    for  _ in range(n):
        a, b = map(int, input().split())
        l.append(a - b)
        
    l.sort()
    
    w = 0
    wyn = 0
    
    for i in range(n - 1, -1, -1):
        w += l[i]
        wyn += 1
        
        if w < 0:
            wyn -= 1
            break
        
        
    print(wyn)
    
main()