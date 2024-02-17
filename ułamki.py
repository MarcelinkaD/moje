import math
from sys import stdin
input = stdin.readline

def main():
    x = str(input().strip())
    ile_miejsc_po_przecinku = len(x)
    jaka_liczba_x = 10 ** ile_miejsc_po_przecinku
    w = int(x)
    jaka_liczba_x -= 1
    gcd = math.gcd(w, jaka_liczba_x)
    w = w // gcd
    jaka_liczba_x = jaka_liczba_x // gcd
    
    print(str(w) + "/" + str(jaka_liczba_x))
    
main()
