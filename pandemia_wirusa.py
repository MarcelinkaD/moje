# https://szkopul.edu.pl/problemset/problem/pandemia_wirusa/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    INF = 1e18
    q = int(input())
    
    for _ in range(q):
        n, s = map(str, input().split())
        n = int(n)
        odl_l, odl_p = [INF for _ in range(n)], [INF for _ in range(n)]
        l, p, zdr = 0, 0, 0
        last = INF
        
        for i in range(n):
            if s[i] == "P":
                last = i
            elif s[i] == "L":
                last = INF
            else:
                if last != INF:
                    odl_p[i] = i - last
                
        last = INF
        
        for i in range(n - 1, -1, -1):
            if s[i] == "L":
                last = i
            elif s[i] == "P":
                last = INF
            else:
                if last != INF:
                    odl_l[i] = last - i
                            
        for i in range(n):
            if s[i] == "P":
                p += 1
            elif s[i] == "L":
                l += 1
            else:
                if odl_p[i] < odl_l[i]:
                    p += 1
                elif odl_p[i] > odl_l[i]:
                    l += 1
                else:
                    zdr += 1
        
        print(l, p, zdr)
                
               
    
main()