# https://szkopul.edu.pl/c/zlo155/p/kaj/21827/

from sys import stdin
input = stdin.readline

def main():
    k = int(input())
    n = int(input())
    l = []
    
    for _ in range(n):
        w = int(input())
        l.append(w)
        
    l.sort()
    l1, l2 = 0, n - 1
    w = 0
    
    while l1 <= l2:
        if l1 == l2:
            w += 1
            break
        else:
            if l[l1] + l[l2] <= k:
                w += 1
                l1 += 1
                l2 -= 1
            else:
                w += 1
                l2 -= 1
                
        
        
        
    print(w)
    
    
main()