# https://szkopul.edu.pl/c/testowy_dd/p/zag/

from sys import stdin
input = stdin.readline

def main():
    s = list(str(input().strip()))
    s.sort()
    litery = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(len(s)):
        if litery[i] != s[i]:
            return litery[i]
        
    return "Z"
    
print(main())