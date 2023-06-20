# https://sio2.mimuw.edu.pl/c/zwo21/p/zol/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def funkcja(li, c, n, k):
    if k * k < n:
        return False
    
    w = 1
    max_szer = -1
    poprzedni = 0
    for i in range(1, n + 1):
        if poprzedni + c[i] <= k:
            poprzedni += c[i]
            max_szer = max(max_szer, poprzedni)
        else:
            w += 1
            poprzedni = c[i]
        
        if w > k:
            return False
    
    if w > k:
        return False
    
    if max_szer > k:
        return False
    
    return True
    

def binary(c, li, n, maxi):
    pocz = maxi
    kon = n
    
    while pocz < kon:
        sr = (pocz + kon) // 2
        if funkcja(li, c, n, sr):
            kon = sr
        else:
            pocz = sr + 1
    
    return pocz

def main():
    n = int(input())
    l = []
    c = {}
    maxi = -1
    
    for k in range(n):
        i = int(input())
        l.append(i)
        c[k + 1] = i
        maxi = max(maxi, i)
        
    print(binary(c, l, n, maxi))
    
main()