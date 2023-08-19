# https://szkopul.edu.pl/c/oki-wakacje-2023/p/obp/

from sys import stdin
input = stdin.readline

def main():
    mon, q = map(int, input().split())
    w = 1
    i = 1
    
    while mon > 0:
        mon -= i * q
        if mon > 0:
            w += 1
            i += 1
        else:
            break
        
    print(w)
    
main()