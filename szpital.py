# https://szkopul.edu.pl/problemset/problem/jpKBED63V04P6iYfisllhv3L/site/?key=statement

from dataclasses import dataclass
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

@dataclass
class pacjent:
    o : str
    index : int

    def __lt__(self, other):
        return self.index < other.index


def main():
    q = int(input())
    kol = []

    for k in range(q):
        i = str(input().strip())

        if i == "ile":
            print(len(kol))
        elif i == "zawolaj":
            w = heappop(kol)
            print(w.o)
        else:
            osoba = i[5:]

            heappush(kol, pacjent(osoba, k + 1))

main()