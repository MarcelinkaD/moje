# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r3b/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    maxi = max(l)
    
    if maxi == 1:
        print(1)
        return
    
    if maxi <= 2:
        print(2)
        return
    
    if n <= 100:
        print(3)
        return
    
    if n <= 1000:
        print(4)
        return
    
    if n % 2 == 0:
        print(5)
        return
    else:
        print(6)
        return
    
    
    
main()