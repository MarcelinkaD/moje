# https://szkopul.edu.pl/problemset/problem/J0gZKwDNMHRCIJ1xpMhzPppG/site/?key=statement

from sys import stdin
input = stdin.readline

def dodaj(k):
    if k == "K" or k == "T" or k == "Q" or k == "J":
        return 10
    else:
        return int(k)
    
def wybierz_naj(akt_w, asy):
    naj = akt_w
    if asy == 0:
        return naj
    else:
        was = asy
        
        for _ in range(asy + 1):
            if was + akt_w <= 21:
                naj = max(was +  akt_w, naj)
            was -= 1
            was += 11
            
        return naj
    
def main():
    n = int(input())
    w = []
    wyn = []
    
    for i in range(n):
        s = str(input().strip())
        akt_w = 0
        asy = 0
        
        for k in s:
            if k != "A":
                akt_w += dodaj(k)
            else:
                asy += 1
        
        if akt_w < 21 and asy != 0:
            akt_w = wybierz_naj(akt_w, asy)
            
        w.append((akt_w, i + 1))
        
    maxi = -1
    
    for i in w:
        if i[0] > maxi and i[0] <= 21:
            maxi = i[0]
            
    for i in w:
        if i[0] == maxi:
            wyn.append(i)
            
    print(len(wyn))
    
    for i in wyn:
        print(i[1], end = " ")
    
main()