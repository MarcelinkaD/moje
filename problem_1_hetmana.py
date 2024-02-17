# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r3a/

from sys import stdin
input = stdin.readline

def main():
    hx, hy = map(int, input().split())
    sx, sy = map(int, input().split())
    
    if hx == sx:
        if hy == sy:
            print(0)
        else:
            print(1)
    else:
        if hy == sy:
            print(1)
        else:
            odlx = max(hx, sx) - min(hx, sx)
            odly = max(hy, sy) - min(hy, sy)
            
            if odlx == odly:
                print(1)
            else:
                print(2)
    
main()