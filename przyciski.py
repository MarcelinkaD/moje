# https://szkopul.edu.pl/c/testowy_dd/p/prz1/18416/

from sys import stdin
input = stdin.readline

def czypo(i, ost_wymaxowanie):
    if ost_wymaxowanie == -1:
        return False
    
    if ost_wymaxowanie < i:
        return True
    
    return False
    
def main():
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    w = [0 for _ in range(n)]
    maxi = -1
    ost_maxi = -1
    czy_byl_od_zmaxowania = set()
    ost_wymaxowanie = -1
    
    for i in range(q):
        if l[i] != n + 1:
            if czypo(i, ost_wymaxowanie) and l[i] not in czy_byl_od_zmaxowania:
                w[l[i] - 1] = ost_maxi + 1
                czy_byl_od_zmaxowania.add(l[i])
            else:
                w[l[i] - 1] += 1
            maxi = max(maxi, w[l[i] - 1])
        else:
            czy_byl_od_zmaxowania = set()
            ost_wymaxowanie = i
            ost_maxi = maxi
            
            
    for i in range(n):
        if i + 1 not in czy_byl_od_zmaxowania and ost_wymaxowanie != -1:
            print(ost_maxi, end = " ")
        else:
            print(w[i], end = " ")
    
main()