# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r3c/

from r3clib import sluchaj, odpowiedz
from sys import stdin
input = stdin.readline

def binary(od, do, x, y, o_co):
    while od < do:
        srodek = (od + do) // 2
        
        if o_co == "x":
            co = sluchaj(srodek, y, srodek, int(1e9) + 7)
            
            if co == -1:
                do = srodek
            elif co == 1:
                od = srodek + 1
            else:
                return srodek
        else:
            co = sluchaj(x, srodek, int(1e9) + 7, srodek)
            
            if co == -1:
                od = srodek + 1
            elif co == 1:
                do = srodek
            else:
                return srodek
                
    return do

def main():
    x, y = 0, 0
    
    x = binary(int(-1e9), int(1e9), x, 0, "x")
    y = binary(int(-1e9), int(1e9), x + 1, 0, "y")
    
    odpowiedz(x, y)
    
main()