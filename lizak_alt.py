# https://szkopul.edu.pl/c/testowy_dd/p/liz1/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    min_w = 1e18
    wystapienia = {}
    
    for i in range(n):
        if l[i] not in wystapienia:
            wystapienia[l[i]] = []
        wystapienia[l[i]].append(i)
        
        if len(wystapienia[l[i]]) >= 3:
            akt_len = len(wystapienia[l[i]])
            odleglosc = i - wystapienia[l[i]][akt_len - 3] + 1
            min_w = min(min_w, odleglosc)
            
    if min_w == 1e18:
        print("NIE")
    else:
        print(min_w)
    
    
main()
