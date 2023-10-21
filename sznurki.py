# https://szkopul.edu.pl/problemset/problem/kX4OlPa45WcHw1SieV6ajTwX/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, wz = map(int, input().split())
    l = list(map(int, input().split()))
    akt_sz = l[0]
    w = n
    
    for i in range(1, n):
        if akt_sz < wz:
            akt_sz += l[i]
            w -= 1
        else:
            akt_sz = l[i]
               
    if akt_sz < wz:
        akt_sz += l[i]
        w -= 1
    else:
        akt_sz = l[i]
            
    print(w)
    
main()