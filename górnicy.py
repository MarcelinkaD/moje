# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r2d/

from sys import stdin
input = stdin.readline

def znajdz_poziom(sektor, N):
    poziom = 0
    while sektor > 1:
        sektor = (sektor - 2) // N + 1
        poziom += 1
    return poziom

def przodek(sektor, N):
    return (sektor - 2) // N + 1

def main():
    q = int(input())
    
    for _ in range(q):
        N, a, b = map(int, input().split())
        
        if N == 1:
            print(min(a, b))
        else:
            poza = znajdz_poziom(a, N)
            pozb = znajdz_poziom(b, N)
            
            while poza > pozb:
                a = przodek(a, N)
                poza -= 1

            while pozb > poza:
                b = przodek(b, N)
                pozb -= 1

            while a != b:
                a = przodek(a, N)
                b = przodek(b, N)
                
            print(a)
            
main()
