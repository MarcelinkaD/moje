# https://szkopul.edu.pl/problemset/problem/vqmkriwEfsMu-sUdZ-xpiZoB/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    w = {}
    kolejnosc = []
    
    for i in range(n):
        z, j = map(int, input().split())
        if z not in w:
            w[z] = 0
            kolejnosc.append(z)
        w[z] += j
        
    print(len(kolejnosc))
    for i in kolejnosc:
        print(i, w[i])
    
main()