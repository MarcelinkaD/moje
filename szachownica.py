# https://szkopul.edu.pl/problemset/problem/hV7ZjgZ9EgSbN9P3HSYIGMLK/site/?key=statement

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    
    if n == 1:
        print("0")
    else:
        if n % 2 == 0:
            nieparz = "01" * (n // 2)
            parz = "10" * (n // 2)
        else:
            nieparz = "01" * (n // 2) + "0"
            parz = "10" * (n // 2) + "1"

        for i in range(1, n + 1):
            if i % 2 == 0:
                print(parz)
            else:
                print(nieparz)

main()