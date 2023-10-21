from sys import stdin 
input = stdin.readline
from bisect import bisect_left

def binary(li, n, pocz, kon):
    i = bisect_left(li, n, pocz, kon)
    if i != len(li) and li[i] == n:
        return i
    else:
        return -1
            

def main(args):
    k, liczba_nastepnych = map(int, input().split())
    liczby = list(map(int, input().split()))
    ile_zostalo = 0
    wynik = False
    liczby = sorted(liczby)

    for i in range(liczba_nastepnych):
        ile_zostalo = k - liczby[i]
        co_w_b = binary(liczby, ile_zostalo, i + 1, liczba_nastepnych)
        
        if co_w_b != -1:
            wynik = True
            print("Mozesz ryzykowac")
            return 0
            
    if wynik == False:
        print("Bez szans")
        return 0
            

if __name__ == '__main__':
    import sys
    main(sys.argv)
