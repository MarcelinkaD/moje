# https://szkopul.edu.pl/c/testowy_dd/p/wie/18801/

from sys import stdin
input = stdin.readline

def main():
    s = str(input())
    n = len(s)
    w = 0
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            w += 1
            
    print(w)
    
main()