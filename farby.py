# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r5c/

from sys import stdin
input = stdin.readline

def main():
    c, z, n = map(int, input().split())
    pot = []
    
    for _ in range(6):
        i = int(input())
        pot.append(i)
        
    wc, wz, wn = pot[4], pot[0], pot[2]
    
    wn += pot[1] / 2
    wz += pot[1] / 2
    
    wn += pot[3] / 2
    wc += pot[3] / 2
    
    wz += pot[5] / 2
    wc += pot[5] / 2
    
    if wc <= c:
        wc = 0
    else:
        wc -= c
        
    if wn <= n:
        wn = 0
    else:
        wn -= n
        
    if wz <= z:
        wz = 0
    else:
        wz -= z
        
    wc = round(wc, 1)
    wz = round(wz, 1)
    wn = round(wn, 1)
    
    if int(wc) == wc and type(wc) != int:
        wc = int(wc)
        
    if int(wz) == wz and type(wz) != int:
        wz = int(wz)
        
    if int(wn) == wn and type(wn) != int:
        wn = int(wn)
    
    print(wc, wz, wn)
    
main()