# https://szkopul.edu.pl/c/oki-wakacje-2023/p/obr/

from sys import stdin
input = stdin.readline

def main():
    n, q = map(int, input().split())
    woj = list(map(int, input().split()))
    
    for _ in range(q):
        l, p, k = map(int, input().split())
        prze = sorted(woj[l - 1 : p], reverse = True)

        print(prze[k - 1])

main()
