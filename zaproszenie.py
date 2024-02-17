# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r2b/

from sys import stdin
input = stdin.readline

def main():
    s, n = map(int, input().split())
    l1 = str(input().strip())
    l2 = str(input().strip())
    kontur, wypelnienie = l1[0], l2[1]
    
    kon = kontur * n
    zwyk = kontur + (wypelnienie * (n - 2)) + kontur
    
    print(kon)
    for _ in range(n - 2):
        print(zwyk)
    print(kon)
    
main()