# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    mamy = sum(l)
    chcemy = (n * (n + 1)) // 2
    
    print(chcemy - mamy)
    
main()