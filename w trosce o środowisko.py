import bisect as b
from sys import stdin
input = stdin.readline

def znajdz(li, n):
    g = b.bisect_left(li, n)
    if g != len(li):
        return g
    else:
        return -1

def is_subsequence(czego_szukam, gdzie, len_gdzie):
    index = -1
    for i in range(len(czego_szukam)):
        litera = czego_szukam[i]
        if litera not in gdzie:
            return False
        
        miejsce = znajdz(gdzie[litera], index + 1)
        if miejsce == -1:
            return False
        
        tmp = gdzie[litera][miejsce]
        
        if index <= tmp:
            index = tmp
        else:
            return False
        
    return True
   
def main():
    t = input().strip()
    n = int(input())
    dic = {}

    for i in range(len(t)):
        if t[i] in dic:
            dic[t[i]].append(i)
        else:
            dic[t[i]] = [i]
        
    for _ in range(n):
        s = input().strip()
        print("TAK" if is_subsequence(s, dic, len(t) - 1) else "NIE")

main()
