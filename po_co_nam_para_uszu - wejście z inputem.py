# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r3c/

from r3clib import sluchaj, odpowiedz
from sys import stdin
input = stdin.readline

def binary(od, do, x, y, o_co, n):
    while od < do:
        srodek = (od + do) // 2
        
        if o_co == "y":
            co = srodek(x, srodek, n, srodek)
            
            if co == -1:
                do = srodek
            else:
                od = srodek + 1
        else:
            co = srodek(srodek, y, srodek, n)
            
            if co == -1:
                do = srodek
            else:
                od = srodek + 1
                
    return srodek

def main():
    n = int(input())
    x, y = 0, 0
    px, py = 0, n
    max_dol = -n
    max_lewo = -n
    max_prawo = n
    max_gora = n
    
    while px != x and py != y:
        gora = sluchaj(x, y, px, py)
        bok = sluchaj(x, y, py, px)
        
        if gora == -1:
            if bok == -1:
                px, py = x - max_lewo // 2, y
                x, y = x - max_lewo // 2, max_dol - y // 2
                max_prawo = x
                max_gora = y
            elif bok == 1:
                px, py = x - max_lewo // 2, max_gora
                x, y = x - max_lewo // 2, max_gora - y // 2
                max_prawo = x
                max_dol = y
            else:
                break
        elif gora == 1:
            if bok == -1:
                px, py = max_prawo - x // 2, max_gora
                x, y = max_prawo - x // 2, max_gora - y // 2
                max_lewo = x
                max_dol = y
            elif bok == 1:
                px, py = max_prawo - x // 2, y
                x, y = max_prawo - x // 2,  max_dol - y // 2
                max_lewo = x
                max_dol = y
            else:
                break
            
    if px != x or py != y:
        if px != x:
            x = binary(max_lewo, max_prawo, x, y, "x", n)
        else:
            y = binary(max_dol, max_gora, x, y, "x", n)
            
    print(x, y)
    
main()
