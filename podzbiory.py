# mamowe oij

from sys import stdin
input = stdin.readline

def Ziuba(ktory, liczba):
    liczba =  (liczba >> ktory)
    return liczba & 1

def main():
    n = int(input())
    l = list(map(str, input().split()))
    wyniki = set()

    for maska in range((2 ** n - 1) + 1):
        akt_w = ""
        for i in range(n):
            if Ziuba(i, maska):
                akt_w += l[i] + " "
        wyniki.add(akt_w)

    wyniki = sorted(list(wyniki))
    for i in wyniki:
        print(i)


main()