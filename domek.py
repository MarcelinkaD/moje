# https://sio2.mimuw.edu.pl/c/oij18-1/p/dom/

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    l = []
    
    for _ in range(n):
        i = str(input().strip())
        l.append(i)
    
    row = ["." for _ in range(m)]
    w = [[row] for _ in range(n)]
    koniec = ["#" for _ in range(m)]
    w[n - 1] = koniec
    
    for j in range(m):
        gdzie = n - 2
        for i in range(n - 2, -1, -1):
            if l[i][j] == "*":
                if l[i + 1][j] == "#":
                    gdzie -= 1
                    continue
            
                w[gdzie][j] = "*"
                l[i][j] = "."
                gdzie -= 1
            elif l[i][j] == "#":
                gdzie = i - 1
                
    for wiersz in l:
        print("".join(wiersz))
    
main()