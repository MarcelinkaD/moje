# https://szkopul.edu.pl/problemset/problem/T8JDkgJLZX_h9Hd_ead-sTum/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    czy_parz = False
    i = 1
    
    for _ in range(n):
        if czy_parz:
            i += n - 1
            for _ in range(i, i - n, -1):
                print(i, end = " ")
                i -= 1
            print("")
            czy_parz = False
            i += n + 1
        else:
            for _ in range(i, i + n):
                print(i, end = " ")
                i += 1
            print("")
            czy_parz = True
            
    
main()