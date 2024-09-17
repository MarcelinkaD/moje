# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/mil/

from sys import stdin
input = stdin.readline

def gasienica(l, n):
    wyn = 0
    for start in range(n):
        produkt = 1
        for i in range(start, n):
            if produkt * l[i] >= 1000000:
                break
            produkt *= l[i]
            wyn += 1
    return wyn

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    l1 = []
    l2 = []
    
    for i in range(n):
        if i % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
            
    print(gasienica(l1, len(l1)) + gasienica(l2, len(l2)))
    
main()