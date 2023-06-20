# https://codeforces.com/problemset/problem/527/A

from sys import stdin
input = stdin.readline

def main():
    a, b = map(int, input().split())
    w = 0
    
    while a > 0 and b > 0:
        if a - b > 0:
            ile_razy = a // b
            a -= ile_razy * b
            w += ile_razy
        else:
            if a == b:
                w += 1
                
            print(w)
            return
        
        if a < b:
            a, b = b, a
    
    if a == b:
        w += 1
                
    print(w)
    return
        
main()