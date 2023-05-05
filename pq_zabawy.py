# https://codeshare.io/Ad9Yvk - algorytmika 19.04

from heapq import heapify, heappop, heappush
from sys import stdin
input = stdin.readline

def main():
    print("Podaj liczbę")
    n = int(input())
    l = [n]
    heapify(l)
    
    while n == n:
        print("Zdejmujemy czy dodajemy?")
        s = str(input().strip())
        
        if s == "zdejmujemy":
            if len(l) == 0:
                print("Pusto wszędzie... Głucho wszędzie...")
            else:
                print(heappop(l))
        else:
            print("Liczba?")
            k = int(input())
            heappush(l, k)
            
        print("Koniec?")
        ans = str(input().strip())
        
        if ans == "TAK" or ans == "YES" or ans == "yes" or ans == "tak":
            break
        
    
main()