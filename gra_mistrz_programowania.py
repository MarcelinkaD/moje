# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r3d/

from sys import stdin
input = stdin.readline

def inRange(x, y, n, m, lista):
    if x < m and y < n:
        if 0 <= x and 0 <= y:
            if lista[y][x] != "#":
                return True
    
    return False

def rozne(ost, akt):
    if ost[1] != akt[1] or ost[0] != akt[0]:
        return True
    return False

def BFS(y, x, graf, koniec, m, n):
    odw = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    kol = []
    kol.append([(y, x)])
    
    while kol:
        sciezka = kol.pop(0)
        wierz = sciezka[-1]
        
        if wierz == koniec:
            return len(sciezka) - 1
        
        for sasiad in graf[(wierz[0], wierz[1])]:
            if not odw[sasiad[0]][sasiad[1]]:
                odw[sasiad[0]][sasiad[1]] = True
                nowa_scie = list(sciezka)
                nowa_scie.append(sasiad)
                kol.append(nowa_scie)
                
    return -1

def main():
    n, m = map(int, input().split())
    lista = []
    
    for k in range(n):
        row = str(input().strip())
        lista.append(row)
        
        for i in range(m):
            if row[i] == "P":
                px = i
                py = k
            elif row[i] == "K":
                kx = i
                ky = k
        
    graf = {}
    
    for i in range(1, n - 1):
        ost = [i, 1]
        for k in range(1, m - 1):
            graf[(i, k)] = []
            graf[(ost[0], ost[1])] = []
            if lista[i][k] != "#" and lista[i][k + 1] == "#":
                graf[(i, k)].append(ost)
                graf[(ost[0], ost[1])].append([i, k])
            elif lista[i][k] == "#":
                ost = [i, k + 1]
    
    for k in range(1, m - 1):
        ost = [1, k]
        for i in range(1, n - 1):
            if lista[i][k] != "#" and lista[i + 1][k] == "#":
                graf[(i, k)].append(ost)
                graf[(ost[0], ost[1])].append([i, k])
            elif lista[i][k] == "#":
                ost = [i + 1, k]
                
    w = BFS(py, px, graf, [ky, kx], m, n)
    
    if px == kx and ky < py and [ky, kx] in graf[(py, px)]:
        w += 1
        
    print(w)
        
main()