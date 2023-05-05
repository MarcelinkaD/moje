# https://codeshare.io/oQZNvL - algorytmika

from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    w = -1
    
    for i in range(n):
        for k in range(max(0, i - k), min(n, i + k)):
            if k == i:
                continue
            w = max(l[i] + l[k], w)
            
    print(w)
    
main()