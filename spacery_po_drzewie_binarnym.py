# https://szkopul.edu.pl/c/testowy_dd/p/spa1/

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    
    for _ in range(q):
        a, b = map(int, input().split())
        w = 0
        
        while a != b:
            if a > b:
                a //= 2
            else:
                b //= 2
            w += 1
            
        print(w)
    
main()