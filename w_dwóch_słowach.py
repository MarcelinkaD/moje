# https://szkopul.edu.pl/c/konkurs-przed-ii-etapem-oij/p/wds/

from sys import stdin
input = stdin.readline

def main():
    n, ile_lini = map(int,input().split())
    l = list(map(str, input().split()))
    ile_uzytych = ile_lini * 2
    
    if ile_uzytych <= n:
        if ile_uzytych % 2 == 0:
            for i in range(ile_uzytych):
                if i % 2 == 0:
                    print(l[i], end = " ")
                else:
                    print(l[i])
        else:
            for i in range(ile_uzytych - 1):
                if i % 2 == 0:
                    print(l[i], end = " ")
                else:
                    print(l[i])
    else:
        if n % 2 == 0:
            for i in range(n):
                if i % 2 == 0:
                    print(l[i], end = " ")
                else:
                    print(l[i])
        else:
            for i in range(n - 1):
                if i % 2 == 0:
                    print(l[i], end = " ")
                else:
                    print(l[i])
    
main()