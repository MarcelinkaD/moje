# https://szkopul.edu.pl/c/testowy_dd/p/per/18809/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    wzor = [i + 1 for i in range(n)]
    
    if wzor != l:
        print("NIE")
        return 0
    else:
        print("TAK")
        return 0
        
main()
    