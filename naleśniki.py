# https://szkopul.edu.pl/problemset/problem/EJyFbR6apT-0OugxvinCNzg3/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    
main()