# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r0c/

from r0clib import podnies, odstaw, do_przodu, do_tylu, w_prawo, w_lewo
from sys import stdin
input = stdin.readline

def main():
    fx, fy = podnies()
    x, y = 0, 0
    
    if fx > x:
        while x < fx:
            w_prawo()
            x += 1
    elif fx < x:
        while x > fx:
            w_lewo()
            x -= 1
            
    if fy > y:    
        while y < fy:
            do_przodu()
            y += 1
    elif fy < y:
        while y > fy:
            do_tylu()
            y -= 1
            
    odstaw()
    
main()
