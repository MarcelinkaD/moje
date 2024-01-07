n = int(input())
akt_badana = 0

while n != 0:
    jedynki = 0
    nowa = akt_badana
    
    while nowa != 0:
        if nowa % 2 == 1:
            jedynki += 1
        nowa //= 2
    
    if jedynki % 2 == 0:
        print(akt_badana)
        n -= 1
        
    akt_badana += 1
    
def brut(n):
    akt_badana = 0

    while n != 0:
        jedynki = 0
        nowa = akt_badana
        
        while nowa != 0:
            if nowa % 2 == 1:
                jedynki += 1
            nowa //= 2
        
        if jedynki % 2 == 0:
            n -= 1
            
            if n == 0:
                print(akt_badana)
            
        akt_badana += 1
