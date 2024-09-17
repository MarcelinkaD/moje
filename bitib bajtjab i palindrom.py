# https://szkopul.edu.pl/problemset/problem/VO4j-mzIwmexYPYvoLGl6uUp/site/?key=statement

from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    c = dict(C(l))

    if n == 1:
        print("TAK")
        return
    else:
        if n % 2 == 1:
            czy_mam_sr = False
            for i in c:
                if c[i] % 2 == 1:
                    if not czy_mam_sr:
                        czy_mam_sr = True
                    else:
                        print("NIE")
                        return
            if czy_mam_sr:
                print("TAK")
            else:
                print("NIE")
        else:
            for i in c:
                if c[i] % 2 == 1:
                    print("NIE")
                    return

            print("TAK")


main()
