# https://szkopul.edu.pl/c/testowy_dd/p/czytanie/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    w = 0
    
    for i in range(n):
        do_przeczytania = l[i]
        
        if do_przeczytania > 10:
            if do_przeczytania % 10 == 0:
                w += (do_przeczytania // 10) - 1
            else:
                w += do_przeczytania // 10        
        
    print(w)
    
main()