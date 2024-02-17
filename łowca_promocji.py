# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r2c/

from sys import stdin
input = stdin.readline            

def order(x):
    return (x[0], x[3])

def main():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    suma = sum(l)
    prze = []

    for _ in range(m):
        co, od, do, nowa = map(int, input().split())
        prze.append((od, co, nowa, "P"))
        prze.append((do + 1, co, nowa, "K"))
        
    prze = sorted(prze, key = lambda x: order(x))
    ile_e_akt_t = 0
    naj_sum = suma
    kiedy = 1
    akt_sum = suma
    
    for i in range(2 * m):
        dzien, co, cena, event = prze[i]
        if event == "P":
            akt_sum -= l[co - 1]
            akt_sum += cena
            
            if akt_sum < naj_sum:
                naj_sum = akt_sum
                kiedy = dzien
        else:
            akt_sum -= cena
            akt_sum += l[co - 1]
            
            if akt_sum < naj_sum:
                naj_sum = akt_sum
                kiedy = dzien
            
    print(naj_sum, kiedy)
        
main()