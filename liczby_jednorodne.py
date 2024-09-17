# https://szkopul.edu.pl/c/marcelina-domin/p/jed/

from sys import stdin
input = stdin.readline

def stworz_licz(x, dlugosc):
    akt_pot = 1
    wyn = 0
    
    while dlugosc > 0:
        wyn += akt_pot * x
        dlugosc -= 1
        akt_pot *= 10
        
    return wyn

def main():
    n = int(input())
    w = []
    dlugosc = len(str(n))
    
    for i in range(1, 10):
        nowa_licz = stworz_licz(i, dlugosc)
        if n < nowa_licz:
            w.append(nowa_licz)
            break
        
    if len(w) == 1:
        for _ in range(3 - len(w)):
            i += 1
            if i < 10:
                nowa_licz = stworz_licz(i, dlugosc)
                w.append(nowa_licz)
    
    if len(w) < 3:
        i = 0
        dlugosc += 1
        for _ in range(3 - len(w)):
            i += 1
            nowa_licz = stworz_licz(i, dlugosc)
            w.append(nowa_licz)
            
    print(w[0], w[1], w[2])

main()