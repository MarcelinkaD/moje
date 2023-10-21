# https://szkopul.edu.pl/problemset/problem/8i6Vamm81hHeI_HqoePmyQJl/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    w = 0
    
    for i in range(n):
        l = list(map(int, input().split()))
        l.sort()
        if l[-1] >= 0:
            w += l[-1]
        
    print(w)
    
main()