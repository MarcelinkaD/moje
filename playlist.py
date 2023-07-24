# https://cses.fi/problemset/task/1141

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    glowa, ogon = -1, 0
    akt_w, max_w = 0, -1
    posiadane = set()
    
    if n == 1:
        print(1)
        return 
    
    while ogon < n - 1:
        while glowa < n - 1 and l[glowa + 1] not in posiadane:
            glowa += 1
            akt_w += 1
            posiadane.add(l[glowa])
            max_w = max(max_w, akt_w)
            
        posiadane.remove(l[ogon])
        akt_w -= 1
        ogon += 1
        
    max_w = max(max_w, akt_w)
        
    print(max_w)
    
main()