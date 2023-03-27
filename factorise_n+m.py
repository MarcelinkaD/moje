# https://codeforces.com/problemset/problem/1740/A

from sys import stdin
input = stdin.readline

def main():
    q = int(input())
    
    for _ in range(q):
        n = int(input())
        
        if n == 2: 
            print(7)
        else:
            print(3)
    
main()