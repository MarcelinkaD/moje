# https://szkopul.edu.pl/c/testowy_dd/p/wie/18801/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    maxi = l[0]
    w = 0
    
    for i in range(1, n):
        w = max(w, maxi - l[i])
        maxi = max(maxi, l[i])
        
    print(w)
    
main()