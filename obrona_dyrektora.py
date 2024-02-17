# https://szkopul.edu.pl/c/mistrz-programowania-2024/p/r4a/

from sys import stdin
input = stdin.readline

def main():
    a, b = map(str, input().split())
    ilegw1 = len(a) - 2
    ilegw2 = len(b) - 2
    
    print(a[0], end = "")
    print("*" * ilegw1, end = "")
    print(a[-1], end = " ")
    
    print(b[0], end = "")
    print("*" * ilegw2, end = "")
    print(b[-1], end = " ")
        
main()