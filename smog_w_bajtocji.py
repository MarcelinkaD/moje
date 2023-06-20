# https://szkopul.edu.pl/c/oki-wakacje-2023/p/smb/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    domy = list(map(int, input().split()))
    mie = list(map(int, input().split()))
    
    domy.sort()
    mie.sort()
    
    suma = sum(domy)
    w = 0
    ost = mie[0]
    
    for i in range(n - 1, -1, -1):
        if suma <= ost:
            print(w)
            return
        
        suma -= domy[i]
        w += 1
    
    print(w)
    
    
main()