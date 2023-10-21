# https://szkopul.edu.pl/problemset/problem/xCD6DZuiNwxyySDwBY_Yx3rV/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    maxi = max(l)
    licznik = 65
    w = ""
    
    for i in range(n):
        if l[i] == maxi:
            w += chr(licznik)
        licznik += 1
        
    print(w)
    
main()