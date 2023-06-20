# https://szkopul.edu.pl/problemset/problem/bbr/site/?key=statement

from sys import stdin
input = stdin.readline

def czy_zla(wy, sz):
    wy *= 4
    sz *= 3
    
    return wy > sz

def main():
    q = int(input())
    
    for _ in range(q):
        sciana = list(map(int, input().split()))
        w = 0
        czy_b = False
        
        for i in range(0, 8, 2):
            a, b = sciana[i], sciana[i + 1]
            
            if czy_zla(a, b):
                print(-1)
                czy_b = True
                break
            else:
                w += a * b
        
        if czy_b == False:
            print(w)
        
        
    
main()
