# https://szkopul.edu.pl/problemset/problem/jBAfHdrPGOGTuFUvaa8lYQhp/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    a = str(input().strip())
    b = str(input().strip())
    duze_b = b.upper()
    wyn = ""
    i = 0

    while i < len(a):
        if i + len(b) <= len(a):
            czy_dod = True
            for k in range(len(b)):
                if a[i + k] != b[k]:
                    czy_dod = False
            
            if czy_dod:
                wyn += duze_b
                i += len(b)
            else:
                wyn += a[i]
                i += 1
        else:
            wyn += a[i]
            i += 1

    print(wyn)

main()
