# https://szkopul.edu.pl/problemset/problem/pDEIAK-vOqP0iPGnUJtPdqV-/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    x, y = map(int, input().split())
    b = -x + (y // 2)
    a = x - b
    
    print(a, b)
    
main()