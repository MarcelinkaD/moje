# https://szkopul.edu.pl/c/olimpiada-poziom-ii-202223/p/kaj/21827/

from sys import stdin
input = stdin.readline

def main():
    maxi = int(input())
    n = int(input())
    l = []
    
    for _ in range(n):
        i = int(input())
        l.append(i)
        
    l.sort()
    
    lewo, prawo = 0, n - 1
    w = 0
    
    while lewo <= prawo:
        if lewo == prawo:
            w += 1
            break
        else:
            if l[lewo] + l[prawo] <= maxi:
                w += 1
                lewo += 1
                prawo -= 1
            else:
                w += 1
                prawo -= 1
            
    print(w)
    
main()