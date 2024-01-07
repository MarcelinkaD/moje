# https://szkopul.edu.pl/problemset/problem/NNLIQigL1hUkl9eTapdOXecR/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = []
    akt_koszt = 0
    
    for _  in range(n):
        a, b = map(int, input().split())
        akt_koszt += a
        l.append(a)
        l.append(b)
        
    wynik = (0, akt_koszt)
    l.sort()
    pop_godzina = 0
    
    for i in range(n):
        godzina = l[i]
        akt_koszt += (-n + i) * (godzina - pop_godzina)
        if akt_koszt < wynik[1]:
            wynik = (godzina, akt_koszt)
        pop_godzina = godzina
        
    print(wynik[0], wynik[1])
    
main()