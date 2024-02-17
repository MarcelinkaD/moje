# https://szkopul.edu.pl/c/testowy_dd/p/kos1/18790/

from sys import stdin
input = stdin.readline

def binary(do, m, akt, trzeba):
    pocz = 0
    kon = do
    
    while pocz < kon:
        srodek = (pocz + kon) // 2
        ile = m * srodek
        
        if akt + ile > trzeba:
            kon = srodek
        elif akt + ile < trzeba:
            pocz = srodek + 1
        else:
            return srodek
    
    return pocz
    
def main():
    akt, trzeba, m = map(int, input().split())
    
    print(binary(trzeba, m, akt, trzeba))
    
main()