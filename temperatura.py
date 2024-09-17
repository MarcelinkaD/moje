# https://szkopul.edu.pl/problemset/problem/viqrxUlcDMjKKcwe9MFNkCQW/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    x = int(input())
    wyn = []

    for i in range(n):
        if l[i] == x:
            wyn.append(i + 1)

    print(len(wyn), end = " ")

    for i in wyn:
        print(i, end = " ")


main()