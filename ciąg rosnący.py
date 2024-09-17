# https://oij.edu.pl/oij18/etap2/zadania/ros/roszad.pdf

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    maxi = max(l)
    wyn_dzielnik = 1000000
    wyn_ile_zostalo = -1
    
    for dzielnik in range(1, maxi + 1):
        ile_zostalo = n
        ost_licz = 0
        czy_git = True
        for i in range(n):
            if l[i] % dzielnik == 0:
                if ost_licz < l[i]:
                    ost_licz = l[i]
                else:
                    czy_git = False
                    break
            else:
                ile_zostalo -= 1
                
        if czy_git:
            if wyn_ile_zostalo < ile_zostalo:
                wyn_ile_zostalo = ile_zostalo
                wyn_dzielnik = dzielnik
                
    print(wyn_dzielnik)
    
main()