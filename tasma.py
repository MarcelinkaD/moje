# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    tab = list(map(int, input().split()))
    pref = [0 for _  in range(n)]
    pref[0] = tab[0]
    w = 1e10
    
    for i in range(1, n):
        pref[i] = pref[i - 1] + tab[i]

    for i in range(n - 1):
        po_lewo = pref[i]
        po_prawo = pref[n - 1] - pref[i]

        w = min(abs(po_lewo - po_prawo), w)
        
    print(w)

main()