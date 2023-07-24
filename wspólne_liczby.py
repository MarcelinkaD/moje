# https://szkopul.edu.pl/c/oki-wakacje-2023/p/wl/

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    l1 = set(map(int, input().split()))
    l2 = set(map(int, input().split()))
    w = sorted(list(l1.intersection(l2)))
    
    if len(w) == 0:
        pass
    else:
        for i in w:
            print(i, end = " ")
    
    
main()

