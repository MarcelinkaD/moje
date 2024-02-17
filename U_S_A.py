# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r2a/

from sys import stdin
input = stdin.readline

def main():
    a, b, c = map(str, input().split())
    
    print(a, b, end = " ")
    
    if c != "Z":
        print(chr(ord(c) + 1))
    else:
        print("A")
    
main()