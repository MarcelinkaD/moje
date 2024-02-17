# https://szkopul.edu.pl/c/testowy_dd/p/kst/18786/

from sys import stdin
input = stdin.readline

def czy_parz(c):
    for i in c:
        if c[i] % 2 == 1:
            return False
    return True

def zle():
    print("NIE")
    quit()

def main():
    n = int(input())
    c = {}
    jakie = set()
    
    for _ in range(n):
        a, b = map(int, input().split())
        
        if a not in c:
            c[a] = 0
            
        if b not in c:
            c[b] = 0
            
        c[a] += 1
        c[b] += 1
        
        jakie.add((a, b))
            
    pocz, kon = 0, 0
    
    if czy_parz(c) == False:
        for i in c:
            if c[i] % 2 == 1:
                if pocz == 0:
                    pocz = i
                else:
                    kon = i
        
        if kon == 0 or (pocz, kon) in jakie or (kon, pocz) in jakie:
            zle()
    else:
        mini = 1e18
        
        for i in c:
            if c[i] < mini:
                mini = c[i]
                pocz, kon = i, i
                
    print(pocz, kon)
    
    
main()