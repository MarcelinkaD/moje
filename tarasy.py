# https://szkopul.edu.pl/problemset/problem/db7CAaN84by8p8oO4jeomOBv/site/?key=statement

from sys import stdin
input = stdin.readline

def g(t, k, n):
    glowa = -1
    ogon = 0
    naj_wyn = -1
    akt_wyn = 0
    akt_kre = k
    
    while ogon < n - 1:
        while glowa < n - 1 and akt_kre >= 0:
            glowa += 1
            akt_kre -= t[glowa]
            
            if akt_kre >= 0:
                akt_wyn += 1
            else:
                break
            
            
            naj_wyn = max(naj_wyn, akt_wyn)
            
        akt_kre += t[ogon]
        ogon += 1
        akt_wyn -= 1
        naj_wyn = max(naj_wyn, akt_wyn)
        
    return naj_wyn

def main():
    n, k = map(int, input().split())
    nowe_t = [0] * n
    tar = []
    
    for i in range(n):
        tar.append(int(input()))
    
    for i in range(n - 1, 0, -1):
        if tar[i] > tar[i - 1]:
            nowe_t[i] = tar[i] - tar[i - 1]
        else:
            nowe_t[i] = 0
    
    tar.reverse()
    for i in range(n - 1, 0, -1):
        if tar[i] > tar[i - 1]:
            tar[i] = tar[i] - tar[i - 1]
        else:
            tar[i] = 0
            
    tar[0] = 0
    nowe_t[0] = 0
    pie = g(nowe_t, k, n)
    dru = g(tar, k, n)
    
    print(max(pie, dru))
    
main()