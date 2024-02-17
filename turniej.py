# https://szkopul.edu.pl/c/testowy_dd/p/tur/18917/

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    
    for _ in range(q):
        n, k = map(int, input().split())
        
        if n < k:
            print(n)
        else:
            print(k - 1)
    
main()