# https://szkopul.edu.pl/c/marcelina-domin/p/baj/

from sys import stdin
input = stdin.readline

def inRange(y, x, n):
    return -1 < y < n and -1 < x < n

def main():
    n = int(input())
    l = []
    w = [[0 for _ in range(n)] for _ in range(n)]
    wyn = 0
    
    for _ in range(n):
        wiersz = str(input().strip())
        l.append(wiersz)
        
    for y in range(n - 1, -1, -1):
        for x in range(n):
            if l[y][x] == "1":
                w[y][x] = 1
                if inRange(y + 1, x - 1, n) and inRange(y + 1, x + 1, n) and l[y + 1][x] == "1":
                    w[y][x] = 1 + min(w[y + 1][x - 1], w[y + 1][x + 1])
                wyn += w[y][x]
            
    print(wyn)
    
main()