# https://szkopul.edu.pl/problemset/problem/EtoosPkK0NsWBseqXHAWrieT/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    ilcznaw, liczkwiat = map(int, input().split())
    kwiaty = str(input().strip())
    ile = list(map(int, input().split()))
    reszta = 0
    zostaly = 0
    
    for i in ile:
        reszta += i
    
    for i in kwiaty:
        if i == "D":
            zostaly += 1
        else:
            co = int(i) - 1
            ile[co] -= 1
            reszta -= 1
            
            if ile[co] == -1:
                print("NIE")
                return
            
    if reszta >= zostaly:
        print("TAK")
    else:
        print("NIE")
    
main()