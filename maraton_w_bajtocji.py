# https://szkopul.edu.pl/c/oki-wakacje-2023/p/mwb/

from sys import stdin
input = stdin.readline

def main():
    w, q, k = map(int, input().split())
    
    for i in range(k - 1):
        w *= q
        
    print(w % 1000000007)
    
main()