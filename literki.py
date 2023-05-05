# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/literki/

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    s = str(input().strip())
    c = C(s)
    w = 0
    
    if "O" not in c or "I" not in c or "G" not in c:
        print(0)
        return 0
    
    while c["O"] != 0 and c["I"] != 0 and c["G"] != 0:
        w += 1
        c["O"] -= 1
        c["I"] -= 1
        c["G"] -= 1
        
    print(w)
    
main()