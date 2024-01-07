# https://szkopul.edu.pl/problemset/problem/h6Bp_7kxcpwFwpa8O4l4wRZj/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    s = str(input().strip())
    ost = 1e18
    
    for i in range(n - 1):
        kan1, kan2 = ord(s[i]), ord(s[i + 1])
        if kan2 < kan1:
            ost = i
            break
        elif kan2 == kan2:
            ost = i
            
    for i in range(n):
        if i != ost:
            print(s[i], end = "")
    
    
    
main()