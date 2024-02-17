# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r5b/

from sys import stdin
input = stdin.readline

def binary(do):
    pocz = 1
    kon = do
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        n = srodek - 1
        gdzie_ost = (n * (n + 1) // 2) + 1
        
        if gdzie_ost < do:
            pocz = srodek + 1
        elif gdzie_ost > do:
            kon = srodek
        else:
            return srodek
        
    return srodek

def main():
    do = int(input())
    
    print(binary(do))
    
main()